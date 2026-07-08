const API_BASE_URL = 'http://127.0.0.1:3000';

async function handleResponse(response, errorMessage) {
  if (!response.ok) {
    throw new Error(errorMessage);
  }

  return response.json();
}

export async function getOrders() {
  const response = await fetch(`${API_BASE_URL}/orders`);
  return handleResponse(response, 'Không thể tải danh sách đơn hàng');
}

export async function createOrder(order) {
  const response = await fetch(`${API_BASE_URL}/orders`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(order)
  });

  return handleResponse(response, 'Không thể lưu đơn hàng');
}

export function generateOrderId() {
  return `o-${Date.now()}`;
}
