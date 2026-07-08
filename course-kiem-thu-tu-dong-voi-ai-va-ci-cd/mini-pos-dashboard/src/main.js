import { getProducts, updateProductStock } from './services/productApi.js';
import { createOrder, generateOrderId } from './services/orderApi.js';
import {
  addItemToCart,
  buildOrderFromCart,
  calculateCartTotal,
  removeItemFromCart
} from './services/cartService.js';
import { formatMoney } from './utils/formatMoney.js';

let products = [];
let cartItems = [];

const productListElement = document.querySelector('[data-testid="product-list"]');
const cartItemsElement = document.querySelector('[data-testid="cart-items"]');
const cartTotalElement = document.querySelector('[data-testid="cart-total"]');
const checkoutButton = document.querySelector('[data-testid="checkout-button"]');
const reloadButton = document.querySelector('[data-testid="reload-button"]');
const messageElement = document.querySelector('[data-testid="message"]');

function showMessage(message, type = 'info') {
  messageElement.textContent = message;
  messageElement.className = `message is-${type}`;
}

function clearMessage() {
  messageElement.textContent = '';
  messageElement.className = 'message';
}

function renderProducts() {
  if (!products.length) {
    productListElement.innerHTML = '<tr><td colspan="6">Chưa có sản phẩm.</td></tr>';
    return;
  }

  productListElement.innerHTML = products
    .map((product) => {
      const isLowStock = Number(product.stock) <= 5;

      return `
        <tr data-testid="product-row-${product.id}">
          <td>${product.code}</td>
          <td>
            <strong>${product.name}</strong>
            ${isLowStock ? '<div class="warning-text">Sắp hết hàng</div>' : ''}
          </td>
          <td>${formatMoney(product.price)}</td>
          <td>
            <span class="stock-badge ${isLowStock ? 'is-low' : ''}" data-testid="product-stock-${product.id}">
              ${product.stock}
            </span>
          </td>
          <td>
            <input
              class="quantity-input"
              data-testid="product-quantity-${product.id}"
              type="number"
              min="1"
              value="1"
              aria-label="Số lượng ${product.name}"
            />
          </td>
          <td>
            <button class="primary-button" data-testid="add-to-cart-${product.id}" data-product-id="${product.id}" type="button">
              Thêm vào giỏ
            </button>
          </td>
        </tr>
      `;
    })
    .join('');
}

function renderCart() {
  if (!cartItems.length) {
    cartItemsElement.innerHTML = '<p class="muted-text">Giỏ hàng đang rỗng.</p>';
    cartTotalElement.textContent = formatMoney(0);
    return;
  }

  cartItemsElement.innerHTML = cartItems
    .map(
      (item) => `
        <div class="cart-item" data-testid="cart-item-${item.productId}">
          <div>
            <strong>${item.name}</strong>
            <small>${formatMoney(item.price)} × ${item.quantity} = ${formatMoney(item.lineTotal)}</small>
          </div>
          <button class="danger-button" data-remove-id="${item.productId}" type="button">Xóa</button>
        </div>
      `
    )
    .join('');

  cartTotalElement.textContent = formatMoney(calculateCartTotal(cartItems));
}

async function loadProducts() {
  clearMessage();
  productListElement.innerHTML = '<tr><td colspan="6">Đang tải sản phẩm...</td></tr>';

  try {
    products = await getProducts();
    renderProducts();
  } catch (error) {
    productListElement.innerHTML = '<tr><td colspan="6">Không thể tải sản phẩm.</td></tr>';
    showMessage(error.message || 'Không thể tải sản phẩm', 'error');
  }
}

function handleAddToCart(productId) {
  const product = products.find((item) => item.id === productId);
  const quantityInput = document.querySelector(`[data-testid="product-quantity-${productId}"]`);
  const quantity = Number(quantityInput?.value);
  const result = addItemToCart(cartItems, product, quantity);

  cartItems = result.cartItems;
  renderCart();
  showMessage(result.message, result.success ? 'success' : 'error');
}

function handleRemoveFromCart(productId) {
  cartItems = removeItemFromCart(cartItems, productId);
  renderCart();
  showMessage('Đã xóa sản phẩm khỏi giỏ hàng', 'info');
}

async function checkout() {
  if (!cartItems.length) {
    showMessage('Giỏ hàng đang rỗng', 'error');
    return;
  }

  try {
    // Kiểm tra lại tồn kho trước khi thanh toán.
    for (const cartItem of cartItems) {
      const product = products.find((item) => item.id === cartItem.productId);

      if (!product || cartItem.quantity > Number(product.stock)) {
        showMessage(`Không đủ hàng trong kho cho sản phẩm ${cartItem.name}`, 'error');
        return;
      }
    }

    // Cập nhật tồn kho từng sản phẩm.
    for (const cartItem of cartItems) {
      const product = products.find((item) => item.id === cartItem.productId);
      const newStock = Number(product.stock) - Number(cartItem.quantity);
      await updateProductStock(product.id, newStock);
    }

    // Lưu lịch sử đơn hàng.
    const order = buildOrderFromCart(cartItems, {
      id: generateOrderId(),
      customerName: 'Khách lẻ',
      createdAt: new Date().toISOString()
    });

    await createOrder(order);

    cartItems = [];
    renderCart();
    await loadProducts();
    showMessage('Thanh toán thành công và đã lưu đơn hàng', 'success');
  } catch (error) {
    showMessage(error.message || 'Thanh toán thất bại', 'error');
  }
}

productListElement.addEventListener('click', (event) => {
  const addButton = event.target.closest('[data-product-id]');

  if (!addButton) {
    return;
  }

  handleAddToCart(addButton.dataset.productId);
});

cartItemsElement.addEventListener('click', (event) => {
  const removeButton = event.target.closest('[data-remove-id]');

  if (!removeButton) {
    return;
  }

  handleRemoveFromCart(removeButton.dataset.removeId);
});

checkoutButton.addEventListener('click', checkout);
reloadButton.addEventListener('click', loadProducts);

document.addEventListener('DOMContentLoaded', async () => {
  renderCart();
  await loadProducts();
});
