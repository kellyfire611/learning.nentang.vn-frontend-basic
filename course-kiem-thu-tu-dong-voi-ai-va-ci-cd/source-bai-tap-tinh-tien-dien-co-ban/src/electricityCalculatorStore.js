export function validateKwh(kwhInput) {
  if (kwhInput === "" || kwhInput === null || kwhInput === undefined) {
    return "Vui long nhap so kWh dien!";
  }

  const parsedKwh = Number(kwhInput);
  if (!Number.isFinite(parsedKwh)) {
    return "So kWh dien phai la so hop le!";
  }

  if (parsedKwh < 0) {
    return "So kWh dien khong duoc am!";
  }

  return "";
}

export function calculateElectricityBill(kwh) {
  let total = 0;

  if (kwh <= 50) {
    return kwh * 1800;
  }

  total += 50 * 1800;

  if (kwh <= 100) {
    return total + (kwh - 50) * 2000;
  }

  total += 50 * 2000;
  total += (kwh - 100) * 2500;

  return total;
}

export function formatCurrencyVnd(amount) {
  return `${Math.round(amount)} VND`;
}

export function calculateElectricityPayment(kwhInput) {
  const kwhError = validateKwh(kwhInput);
  if (kwhError) {
    return kwhError;
  }

  const parsedKwh = Number(kwhInput);
  const totalAmount = calculateElectricityBill(parsedKwh);

  return `So tien dien can tra: ${formatCurrencyVnd(totalAmount)}`;
}

if (typeof window !== "undefined") {
  window.calculateElectricityPayment = calculateElectricityPayment;
}
