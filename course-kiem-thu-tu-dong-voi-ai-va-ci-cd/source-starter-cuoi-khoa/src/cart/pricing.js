export function formatCurrency(value) {
  return `${value.toLocaleString("vi-VN")} đ`;
}

export function normalizeCoupon(code) {
  return String(code || "").trim().toUpperCase();
}

export function validateQuantity(quantity) {
  if (!Number.isInteger(quantity) || quantity < 1 || quantity > 10) {
    throw new Error("So luong phai la so nguyen trong khoang 1-10.");
  }

  return quantity;
}

function getSubtotal(items) {
  return items.reduce((total, item) => total + item.price * item.quantity, 0);
}

function getItemCount(items) {
  return items.reduce((count, item) => count + item.quantity, 0);
}

export function calculateShipping(subtotalAfterDiscount, couponCode) {
  if (normalizeCoupon(couponCode) === "FREESHIP") {
    return 0;
  }

  return subtotalAfterDiscount >= 800000 ? 0 : 30000;
}

export function getCouponDiscount(subtotal, itemCount, couponCode) {
  const normalized = normalizeCoupon(couponCode);

  if (!normalized) {
    return {
      appliedCoupon: "",
      discount: 0,
      note: "Chua ap dung ma giam gia."
    };
  }

  if (normalized === "SAVE10") {
    if (subtotal < 500000) {
      return {
        appliedCoupon: "",
        discount: 0,
        note: "Ma SAVE10 chi ap dung tu 500.000 đ."
      };
    }

    return {
      appliedCoupon: normalized,
      discount: Math.round(subtotal * 0.1),
      note: "Da ap dung giam 10% cho don hang."
    };
  }

  if (normalized === "COMBO15") {
    if (subtotal < 1000000 || itemCount < 3) {
      return {
        appliedCoupon: "",
        discount: 0,
        note: "COMBO15 can it nhat 3 san pham va tam tinh tu 1.000.000 đ."
      };
    }

    return {
      appliedCoupon: normalized,
      discount: Math.round(subtotal * 0.15),
      note: "Da ap dung COMBO15 cho don hang lon."
    };
  }

  if (normalized === "FREESHIP") {
    return {
      appliedCoupon: normalized,
      discount: 0,
      note: "Da ap dung mien phi van chuyen."
    };
  }

  return {
    appliedCoupon: "",
    discount: 0,
    note: "Ma giam gia khong hop le."
  };
}

export function calculateSummary(items, couponCode = "") {
  const subtotal = getSubtotal(items);
  const itemCount = getItemCount(items);
  const couponResult = getCouponDiscount(subtotal, itemCount, couponCode);
  const subtotalAfterDiscount = Math.max(subtotal - couponResult.discount, 0);
  const shipping = itemCount === 0 ? 0 : calculateShipping(subtotalAfterDiscount, couponResult.appliedCoupon);
  const total = subtotalAfterDiscount + shipping;

  return {
    itemCount,
    subtotal,
    discount: couponResult.discount,
    shipping,
    total,
    appliedCoupon: couponResult.appliedCoupon,
    note: couponResult.note
  };
}