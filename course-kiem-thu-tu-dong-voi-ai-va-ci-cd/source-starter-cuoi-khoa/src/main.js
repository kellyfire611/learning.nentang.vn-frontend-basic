import { createCart } from "./cart/cart.js";
import { formatCurrency } from "./cart/pricing.js";
import { products } from "./data/products.js";

const cart = createCart(products);

const elements = {
  productList: document.querySelector("#product-list"),
  searchInput: document.querySelector("#search-input"),
  cartItems: document.querySelector("#cart-items"),
  cartCount: document.querySelector("#cart-count"),
  couponInput: document.querySelector("#coupon-input"),
  applyCoupon: document.querySelector("#apply-coupon"),
  statusMessage: document.querySelector("#status-message"),
  cartSubtotal: document.querySelector("#cart-subtotal"),
  cartDiscount: document.querySelector("#cart-discount"),
  cartShipping: document.querySelector("#cart-shipping"),
  cartTotal: document.querySelector("#cart-total")
};

function renderProducts(keyword = "") {
  const normalizedKeyword = keyword.trim().toLowerCase();
  const matchedProducts = products.filter((product) => {
    const haystack = `${product.name} ${product.category} ${product.description}`.toLowerCase();
    return haystack.includes(normalizedKeyword);
  });

  if (!matchedProducts.length) {
    elements.productList.innerHTML = '<div class="empty-state">Khong tim thay san pham phu hop.</div>';
    return;
  }

  elements.productList.innerHTML = matchedProducts.map((product) => `
    <article class="product-card" data-testid="product-card-${product.id}">
      <div>
        <p class="eyebrow">${product.category}</p>
        <h3>${product.name}</h3>
        <p>${product.description}</p>
      </div>
      <div class="price-row">
        <span class="price">${formatCurrency(product.price)}</span>
        <button type="button" data-testid="add-to-cart-${product.id}" data-product-id="${product.id}">Them vao gio</button>
      </div>
    </article>
  `).join("");

  elements.productList.querySelectorAll("button[data-product-id]").forEach((button) => {
    button.addEventListener("click", () => {
      const productId = Number(button.dataset.productId);
      cart.addItem(productId);
      updateStatus("Da them san pham vao gio hang.");
      renderCart();
    });
  });
}

function renderCart() {
  const { items, summary } = cart.getState();
  elements.cartCount.textContent = String(summary.itemCount);
  elements.cartSubtotal.textContent = formatCurrency(summary.subtotal);
  elements.cartDiscount.textContent = formatCurrency(summary.discount);
  elements.cartShipping.textContent = formatCurrency(summary.shipping);
  elements.cartTotal.textContent = formatCurrency(summary.total);

  if (!items.length) {
    elements.cartItems.innerHTML = '<div class="empty-state">Gio hang dang trong. Hay them san pham de test.</div>';
    return;
  }

  elements.cartItems.innerHTML = items.map((item) => `
    <section class="cart-row" data-testid="cart-row-${item.id}">
      <div class="cart-row-header">
        <div>
          <h3>${item.name}</h3>
          <p>${formatCurrency(item.price)} x ${item.quantity}</p>
        </div>
        <strong>${formatCurrency(item.price * item.quantity)}</strong>
      </div>
      <div class="cart-line-bottom">
        <label class="qty-box">
          <span>So luong</span>
          <input
            class="qty-input"
            data-testid="qty-input-${item.id}"
            data-qty-id="${item.id}"
            type="number"
            min="1"
            max="10"
            step="1"
            value="${item.quantity}"
          />
        </label>
        <button class="remove-button" data-testid="remove-item-${item.id}" data-remove-id="${item.id}" type="button">Xoa</button>
      </div>
    </section>
  `).join("");

  elements.cartItems.querySelectorAll("[data-remove-id]").forEach((button) => {
    button.addEventListener("click", () => {
      cart.removeItem(Number(button.dataset.removeId));
      updateStatus("Da xoa san pham khoi gio hang.");
      renderCart();
    });
  });

  elements.cartItems.querySelectorAll("[data-qty-id]").forEach((input) => {
    input.addEventListener("change", () => {
      try {
        cart.updateQuantity(Number(input.dataset.qtyId), Number(input.value));
        updateStatus("Da cap nhat so luong san pham.");
        renderCart();
      } catch (error) {
        input.value = String(cart.getState().items.find((item) => item.id === Number(input.dataset.qtyId))?.quantity || 1);
        updateStatus(error.message);
      }
    });
  });
}

function updateStatus(message) {
  const note = cart.getSummary().note;
  elements.statusMessage.textContent = note && note !== "Chua ap dung ma giam gia." ? `${message} ${note}` : message;
}

elements.searchInput.addEventListener("input", (event) => {
  renderProducts(event.target.value);
});

elements.applyCoupon.addEventListener("click", () => {
  cart.setCoupon(elements.couponInput.value);
  renderCart();
  updateStatus(cart.getSummary().note);
});

renderProducts();
renderCart();