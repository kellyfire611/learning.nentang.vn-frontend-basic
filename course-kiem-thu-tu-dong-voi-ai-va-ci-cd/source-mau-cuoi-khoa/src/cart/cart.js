import { calculateSummary, normalizeCoupon, validateQuantity } from "./pricing.js";

function cloneItems(items) {
  return items.map((item) => ({ ...item }));
}

export function createCart(productCatalog) {
  const productsById = new Map(productCatalog.map((product) => [product.id, { ...product }]));
  const state = {
    items: [],
    couponCode: ""
  };

  function getCartItem(productId) {
    return state.items.find((item) => item.id === productId);
  }

  function addItem(productId, quantity = 1) {
    const product = productsById.get(productId);
    if (!product) {
      throw new Error("San pham khong ton tai.");
    }

    const safeQuantity = validateQuantity(quantity);
    const existingItem = getCartItem(productId);

    if (existingItem) {
      existingItem.quantity = validateQuantity(existingItem.quantity + safeQuantity);
      return getState();
    }

    state.items.push({
      id: product.id,
      name: product.name,
      price: product.price,
      quantity: safeQuantity
    });

    return getState();
  }

  function removeItem(productId) {
    state.items = state.items.filter((item) => item.id !== productId);
    return getState();
  }

  function updateQuantity(productId, quantity) {
    const existingItem = getCartItem(productId);
    if (!existingItem) {
      throw new Error("Khong tim thay san pham trong gio hang.");
    }

    existingItem.quantity = validateQuantity(quantity);
    return getState();
  }

  function setCoupon(code) {
    state.couponCode = normalizeCoupon(code);
    return getState();
  }

  function clear() {
    state.items = [];
    state.couponCode = "";
    return getState();
  }

  function getSummary() {
    return calculateSummary(state.items, state.couponCode);
  }

  function getState() {
    return {
      items: cloneItems(state.items),
      couponCode: state.couponCode,
      summary: getSummary()
    };
  }

  return {
    addItem,
    removeItem,
    updateQuantity,
    setCoupon,
    clear,
    getState,
    getSummary
  };
}