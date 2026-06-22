let apiBaseUrl = getDefaultApiBaseUrl();

function getDefaultApiBaseUrl() {
  try {
    if (import.meta.env?.VITE_API_BASE_URL) {
      return import.meta.env.VITE_API_BASE_URL;
    }
  } catch {
    // Vitest/Vite có import.meta.env, môi trường khác thì bỏ qua.
  }

  return 'http://localhost:3000';
}

export function setApiBaseUrl(baseUrl) {
  apiBaseUrl = String(baseUrl).replace(/\/$/, '');
}

export function getApiBaseUrl() {
  return apiBaseUrl;
}

async function request(path, options = {}) {
  const response = await fetch(`${apiBaseUrl}${path}`, {
    headers: {
      'Content-Type': 'application/json',
      ...(options.headers ?? {}),
    },
    ...options,
  });

  if (!response.ok) {
    let message = `API error ${response.status}`;

    try {
      const body = await response.json();
      message = body.message || body.error || message;
    } catch {
      // Response không phải JSON thì dùng message mặc định.
    }

    throw new Error(message);
  }

  if (response.status === 204) {
    return null;
  }

  const text = await response.text();
  return text ? JSON.parse(text) : null;
}

export function fetchCustomers() {
  return request('/customers', {
    method: 'GET',
  });
}

export function createCustomer(customer) {
  return request('/customers', {
    method: 'POST',
    body: JSON.stringify(customer),
  });
}

export function updateCustomer(id, customer) {
  return request(`/customers/${id}`, {
    method: 'PUT',
    body: JSON.stringify(customer),
  });
}

export function patchCustomerStatus(id, status) {
  return request(`/customers/${id}`, {
    method: 'PATCH',
    body: JSON.stringify({ status }),
  });
}

export function deleteCustomer(id) {
  return request(`/customers/${id}`, {
    method: 'DELETE',
  });
}
