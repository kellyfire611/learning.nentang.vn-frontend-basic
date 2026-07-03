const API_BASE_URL = 'http://localhost:3000';

async function request(url, options = {}) {
  const response = await fetch(url, {
    headers: {
      'Content-Type': 'application/json',
      ...(options.headers || {})
    },
    ...options
  });

  if (!response.ok) {
    let message = `API error: ${response.status}`;
    try {
      const data = await response.json();
      message = data.message || message;
    } catch {
      // JSON Server không phải lúc nào cũng trả JSON khi lỗi.
    }
    throw new Error(message);
  }

  if (response.status === 204) {
    return null;
  }

  return response.json();
}

export async function getData(resource) {
  return request(`${API_BASE_URL}/${resource}`);
}

export async function getDataById(resource, id) {
  return request(`${API_BASE_URL}/${resource}/${id}`);
}

export async function createData(resource, data) {
  return request(`${API_BASE_URL}/${resource}`, {
    method: 'POST',
    body: JSON.stringify(data)
  });
}

export async function updateData(resource, id, data) {
  return request(`${API_BASE_URL}/${resource}/${id}`, {
    method: 'PUT',
    body: JSON.stringify(data)
  });
}

export async function patchData(resource, id, data) {
  return request(`${API_BASE_URL}/${resource}/${id}`, {
    method: 'PATCH',
    body: JSON.stringify(data)
  });
}

export async function deleteData(resource, id) {
  return request(`${API_BASE_URL}/${resource}/${id}`, {
    method: 'DELETE'
  });
}
