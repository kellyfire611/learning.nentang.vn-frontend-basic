const API_URL = 'http://127.0.0.1:3000/products';

export async function getProducts() {
  const response = await fetch(API_URL);

  if (!response.ok) {
    throw new Error('Không tải được danh sách sản phẩm');
  }

  return response.json();
}

export async function updateProductStock(productId, newStock) {
  const response = await fetch(`${API_URL}/${productId}`, {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      stock: newStock
    })
  });

  if (!response.ok) {
    throw new Error('Không cập nhật được tồn kho');
  }

  return response.json();
}
