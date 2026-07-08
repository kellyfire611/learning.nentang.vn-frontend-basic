const API_BASE_URL = 'http://127.0.0.1:3000';

async function handleResponse(response, errorMessage) {
  if (!response.ok) {
    throw new Error(errorMessage);
  }

  return response.json();
}

export async function getProducts() {
  const response = await fetch(`${API_BASE_URL}/products`);
  return handleResponse(response, 'Không thể tải danh sách sản phẩm');
}

export async function updateProductStock(productId, newStock) {
  const response = await fetch(`${API_BASE_URL}/products/${productId}`, {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ stock: newStock })
  });

  return handleResponse(response, 'Không thể cập nhật tồn kho sản phẩm');
}
