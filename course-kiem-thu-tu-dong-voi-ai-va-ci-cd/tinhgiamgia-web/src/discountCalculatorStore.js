export function validatePrice(priceInput) {
  if (priceInput === "" || priceInput === null || priceInput === undefined) {
    return "Vui lòng nhập giá gốc!";
  }

  const parsedPrice = Number(priceInput);
  if (!Number.isFinite(parsedPrice) || parsedPrice <= 0) {
    return "Giá gốc phải là số lớn hơn 0!";
  }

  return "";
}

export function validateDiscountPercent(discountPercentInput) {
  if (
    discountPercentInput === "" ||
    discountPercentInput === null ||
    discountPercentInput === undefined
  ) {
    return "Vui lòng nhập phần trăm giảm giá!";
  }

  const parsedDiscountPercent = Number(discountPercentInput);
  if (
    !Number.isFinite(parsedDiscountPercent) ||
    parsedDiscountPercent < 0 ||
    parsedDiscountPercent > 100
  ) {
    return "Phần trăm giảm giá phải từ 0 đến 100!";
  }

  return "";
}

export function calculateFinalPrice(price, discountPercent) {
  const discountAmount = (price * discountPercent) / 100;
  return price - discountAmount;
}

export function formatCurrencyVnd(amount) {
  return `${Math.round(amount)} VNĐ`;
}

export function calculatePayment(priceInput, discountPercentInput) {
  const priceError = validatePrice(priceInput);
  if (priceError) {
    return priceError;
  }

  const discountError = validateDiscountPercent(discountPercentInput);
  if (discountError) {
    return discountError;
  }

  const parsedPrice = Number(priceInput);
  const parsedDiscountPercent = Number(discountPercentInput);
  const finalPrice = calculateFinalPrice(parsedPrice, parsedDiscountPercent);

  return `Số tiền cần trả: ${formatCurrencyVnd(finalPrice)}`;
}

if (typeof window !== "undefined") {
  window.calculatePayment = calculatePayment;
}
