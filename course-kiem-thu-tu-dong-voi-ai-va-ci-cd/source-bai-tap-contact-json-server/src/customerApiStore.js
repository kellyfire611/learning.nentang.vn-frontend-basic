export const CUSTOMER_API_URL = "http://localhost:3001/customers";

function buildCustomerUrl(id) {
  return `${CUSTOMER_API_URL}/${id}`;
}

async function parseJson(response) {
  return response.json();
}

export async function fetchCustomers(fetchFn = fetch) {
  const response = await fetchFn(CUSTOMER_API_URL);

  if (!response.ok) {
    throw new Error("Không thể tải danh sách khách hàng!");
  }

  return parseJson(response);
}

export async function fetchCustomerById(id, fetchFn = fetch) {
  const response = await fetchFn(buildCustomerUrl(id));

  if (!response.ok) {
    throw new Error("Không thể tải thông tin khách hàng!");
  }

  return parseJson(response);
}

export async function createCustomer(customer, fetchFn = fetch) {
  const response = await fetchFn(CUSTOMER_API_URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(customer),
  });

  if (!response.ok) {
    throw new Error("Không thể thêm khách hàng!");
  }

  return parseJson(response);
}

export async function updateCustomer(id, customer, fetchFn = fetch) {
  const response = await fetchFn(buildCustomerUrl(id), {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(customer),
  });

  if (!response.ok) {
    throw new Error("Không thể cập nhật khách hàng!");
  }

  return parseJson(response);
}

export async function patchCustomerStatus(id, status, fetchFn = fetch) {
  const response = await fetchFn(buildCustomerUrl(id), {
    method: "PATCH",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ status }),
  });

  if (!response.ok) {
    throw new Error("Không thể cập nhật trạng thái khách hàng!");
  }

  return parseJson(response);
}

export async function patchCustomerFavorite(id, isFavorite, fetchFn = fetch) {
  const response = await fetchFn(buildCustomerUrl(id), {
    method: "PATCH",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ isFavorite }),
  });

  if (!response.ok) {
    throw new Error("Không thể cập nhật khách hàng yêu thích!");
  }

  return parseJson(response);
}

export async function deleteCustomer(id, fetchFn = fetch) {
  const response = await fetchFn(buildCustomerUrl(id), {
    method: "DELETE",
  });

  if (!response.ok) {
    throw new Error("Không thể xóa khách hàng!");
  }

  return parseJson(response);
}

if (typeof window !== "undefined") {
  window.customerApiStore = {
    fetchCustomers,
    fetchCustomerById,
    createCustomer,
    updateCustomer,
    patchCustomerStatus,
    patchCustomerFavorite,
    deleteCustomer,
  };
}
