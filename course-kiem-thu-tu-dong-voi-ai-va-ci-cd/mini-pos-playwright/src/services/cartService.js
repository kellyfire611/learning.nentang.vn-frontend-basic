// File này chứa logic nghiệp vụ thuần.
// Không phụ thuộc DOM, nên có thể unit test bằng Vitest.

export function validateQuantity(quantity, stock) {
  const numberQuantity = Number(quantity);

  if (!Number.isInteger(numberQuantity)) {
    return {
      valid: false,
      message: 'Số lượng phải là số nguyên'
    };
  }

  if (numberQuantity <= 0) {
    return {
      valid: false,
      message: 'Số lượng phải lớn hơn 0'
    };
  }

  if (numberQuantity > stock) {
    return {
      valid: false,
      message: 'Số lượng vượt quá tồn kho'
    };
  }

  return {
    valid: true,
    message: ''
  };
}

export function calculateLineTotal(price, quantity) {
  return Number(price) * Number(quantity);
}

export function calculateCartTotal(cartItems) {
  return cartItems.reduce((total, item) => {
    return total + calculateLineTotal(item.price, item.quantity);
  }, 0);
}

export function updateStockAfterCheckout(products, cartItems) {
  return products.map((product) => {
    const cartItem = cartItems.find((item) => String(item.id) === String(product.id));

    if (!cartItem) {
      return product;
    }

    return {
      ...product,
      stock: product.stock - cartItem.quantity
    };
  });
}

export function addItemToCart(cartItems, product, quantity) {
  const numberQuantity = Number(quantity);
  const existingItem = cartItems.find((item) => String(item.id) === String(product.id));

  if (!existingItem) {
    return [
      ...cartItems,
      {
        id: product.id,
        code: product.code,
        name: product.name,
        price: product.price,
        quantity: numberQuantity
      }
    ];
  }

  return cartItems.map((item) => {
    if (String(item.id) !== String(product.id)) {
      return item;
    }

    return {
      ...item,
      quantity: item.quantity + numberQuantity
    };
  });
}
