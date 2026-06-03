const CUSTOMER_API_URL = "https://jsonplaceholder.typicode.com/users";

export async function fetchCustomers(fetchFn = fetch) {
  const response = await fetchFn(CUSTOMER_API_URL);

  if (!response.ok) {
    throw new Error("Khong the tai danh sach khach hang!");
  }

  return response.json();
}

export function validateCustomers(customers) {
  if (!Array.isArray(customers) || customers.length === 0) {
    return false;
  }

  const firstCustomer = customers[0];

  return Boolean(
    firstCustomer &&
      "id" in firstCustomer &&
      "name" in firstCustomer &&
      "email" in firstCustomer
  );
}

export function formatCustomerList(customers) {
  return customers.map(function (customer) {
    return `${customer.id}. ${customer.name} - ${customer.email}`;
  });
}

if (typeof window !== "undefined") {
  window.customerApiStore = {
    fetchCustomers,
    validateCustomers,
    formatCustomerList,
  };
}
