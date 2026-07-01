import {
  addItemToCart,
  calculateCartTotal,
  calculateLineTotal,
  validateQuantity
} from './services/cartService.js';
import {
  getProducts,
  updateProductStock
} from './services/productApi.js';
import { formatMoney } from './utils/formatMoney.js';

let products = [];
let cartItems = [];

const productListEl = document.querySelector('#product-list');
const cartItemsEl = document.querySelector('#cart-items');
const cartTotalEl = document.querySelector('#cart-total');
const checkoutButtonEl = document.querySelector('#checkout-button');
const messageEl = document.querySelector('#message');
const reloadButtonEl = document.querySelector('#reload-button');

function showMessage(message, type = 'success') {
  messageEl.textContent = message;
  messageEl.className = `message ${type}`;
}

function hideMessage() {
  messageEl.textContent = '';
  messageEl.className = 'message hidden';
}

function findProduct(productId) {
  return products.find((product) => String(product.id) === String(productId));
}

function renderProducts() {
  if (products.length === 0) {
    productListEl.innerHTML = `
      <tr>
        <td colspan="6">Không có sản phẩm</td>
      </tr>
    `;
    return;
  }

  productListEl.innerHTML = products.map((product) => {
    return `
      <tr data-testid="product-row-${product.id}">
        <td>${product.code}</td>
        <td>
          <div class="product-name">${product.name}</div>
        </td>
        <td>${formatMoney(product.price)}</td>
        <td>
          <span
            class="stock-badge"
            data-testid="product-stock-${product.id}"
          >
            ${product.stock}
          </span>
        </td>
        <td>
          <input
            data-testid="product-quantity-${product.id}"
            type="number"
            min="1"
            value="1"
          />
        </td>
        <td>
          <button
            class="add-button"
            data-testid="add-to-cart-${product.id}"
            data-product-id="${product.id}"
            ${product.stock <= 0 ? 'disabled' : ''}
          >
            Thêm vào giỏ
          </button>
        </td>
      </tr>
    `;
  }).join('');
}

function renderCart() {
  if (cartItems.length === 0) {
    cartItemsEl.innerHTML = 'Giỏ hàng trống';
    cartTotalEl.textContent = formatMoney(0);
    return;
  }

  cartItemsEl.innerHTML = cartItems.map((item) => {
    const lineTotal = calculateLineTotal(item.price, item.quantity);

    return `
      <div class="cart-item" data-testid="cart-item-${item.id}">
        <div class="cart-item-title">
          <span>${item.name}</span>
          <span>${formatMoney(lineTotal)}</span>
        </div>
        <div class="cart-item-meta">
          ${item.quantity} x ${formatMoney(item.price)}
        </div>
      </div>
    `;
  }).join('');

  cartTotalEl.textContent = formatMoney(calculateCartTotal(cartItems));
}

function getQuantityFromInput(productId) {
  const quantityInput = document.querySelector(`[data-testid="product-quantity-${productId}"]`);
  return Number(quantityInput.value);
}

function handleAddToCart(productId) {
  hideMessage();

  const product = findProduct(productId);
  const quantity = getQuantityFromInput(productId);
  const existingCartItem = cartItems.find((item) => String(item.id) === String(productId));
  const currentQuantityInCart = existingCartItem ? existingCartItem.quantity : 0;
  const availableStock = product.stock - currentQuantityInCart;

  const validation = validateQuantity(quantity, availableStock);

  if (!validation.valid) {
    showMessage(validation.message, 'error');
    return;
  }

  cartItems = addItemToCart(cartItems, product, quantity);
  renderCart();
  showMessage('Đã thêm sản phẩm vào giỏ hàng', 'success');
}

async function handleCheckout() {
  hideMessage();

  if (cartItems.length === 0) {
    showMessage('Giỏ hàng đang rỗng', 'error');
    return;
  }

  try {
    for (const item of cartItems) {
      const product = findProduct(item.id);
      const newStock = product.stock - item.quantity;
      await updateProductStock(product.id, newStock);
    }

    cartItems = [];
    products = await getProducts();

    renderProducts();
    renderCart();
    showMessage('Thanh toán thành công', 'success');
  } catch (error) {
    showMessage(error.message, 'error');
  }
}

async function loadProducts() {
  try {
    hideMessage();
    products = await getProducts();
    renderProducts();
    renderCart();
  } catch (error) {
    showMessage(error.message, 'error');
  }
}

productListEl.addEventListener('click', (event) => {
  const button = event.target.closest('[data-product-id]');

  if (!button) {
    return;
  }

  handleAddToCart(button.dataset.productId);
});

checkoutButtonEl.addEventListener('click', handleCheckout);
reloadButtonEl.addEventListener('click', loadProducts);

loadProducts();
