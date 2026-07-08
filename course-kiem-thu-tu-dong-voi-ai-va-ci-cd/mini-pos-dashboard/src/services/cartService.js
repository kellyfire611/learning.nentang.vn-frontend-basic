export function calculateLineTotal(item) {
  const price = Number(item?.price) || 0;
  const quantity = Number(item?.quantity) || 0;

  return price * quantity;
}

export function calculateCartTotal(items) {
  if (!Array.isArray(items)) {
    return 0;
  }

  return items.reduce((sum, item) => sum + calculateLineTotal(item), 0);
}

export function validateQuantity(product, quantity, quantityAlreadyInCart = 0) {
  const parsedQuantity = Number(quantity);

  if (!Number.isInteger(parsedQuantity) || parsedQuantity <= 0) {
    return {
      valid: false,
      message: 'Số lượng phải là số nguyên lớn hơn 0'
    };
  }

  if (!product) {
    return {
      valid: false,
      message: 'Không tìm thấy sản phẩm'
    };
  }

  const requestedQuantity = parsedQuantity + Number(quantityAlreadyInCart || 0);

  if (requestedQuantity > Number(product.stock)) {
    return {
      valid: false,
      message: 'Không đủ hàng trong kho'
    };
  }

  return {
    valid: true,
    message: 'Số lượng hợp lệ'
  };
}

export function addItemToCart(cartItems, product, quantity) {
  const currentItems = Array.isArray(cartItems) ? [...cartItems] : [];
  const parsedQuantity = Number(quantity);
  const existingItem = currentItems.find((item) => item.productId === product.id);
  const quantityAlreadyInCart = existingItem?.quantity || 0;
  const validation = validateQuantity(product, parsedQuantity, quantityAlreadyInCart);

  if (!validation.valid) {
    return {
      success: false,
      message: validation.message,
      cartItems: currentItems
    };
  }

  if (existingItem) {
    existingItem.quantity += parsedQuantity;
    existingItem.lineTotal = calculateLineTotal(existingItem);
  } else {
    currentItems.push({
      productId: product.id,
      code: product.code,
      name: product.name,
      price: product.price,
      quantity: parsedQuantity,
      lineTotal: product.price * parsedQuantity
    });
  }

  return {
    success: true,
    message: 'Đã thêm sản phẩm vào giỏ hàng',
    cartItems: currentItems
  };
}

export function removeItemFromCart(cartItems, productId) {
  if (!Array.isArray(cartItems)) {
    return [];
  }

  return cartItems.filter((item) => item.productId !== productId);
}

export function buildOrderFromCart(cartItems, options = {}) {
  const items = Array.isArray(cartItems) ? cartItems : [];

  return {
    id: options.id,
    customerName: options.customerName || 'Khách lẻ',
    items: items.map((item) => ({
      productId: item.productId,
      code: item.code,
      name: item.name,
      price: item.price,
      quantity: item.quantity,
      lineTotal: calculateLineTotal(item)
    })),
    totalAmount: calculateCartTotal(items),
    createdAt: options.createdAt || new Date().toISOString()
  };
}
