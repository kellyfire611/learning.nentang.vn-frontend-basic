export const CUSTOMER_STATUS = {
  NEW: 'new',
  CONTACTED: 'contacted',
  REGISTERED: 'registered',
};

export const CUSTOMER_STATUS_LABEL = {
  [CUSTOMER_STATUS.NEW]: 'Khách mới',
  [CUSTOMER_STATUS.CONTACTED]: 'Đã tư vấn',
  [CUSTOMER_STATUS.REGISTERED]: 'Đã đăng ký',
};

export function normalizeText(value) {
  return String(value ?? '').trim();
}

export function validateCustomerForm(formData) {
  const fullName = normalizeText(formData.fullName);
  const phone = normalizeText(formData.phone);
  const email = normalizeText(formData.email);
  const course = normalizeText(formData.course);

  const errors = {};

  if (!fullName) {
    errors.fullName = 'Họ tên không được rỗng';
  } else if (fullName.length < 3) {
    errors.fullName = 'Họ tên phải có tối thiểu 3 ký tự';
  }

  if (!phone) {
    errors.phone = 'Số điện thoại không được rỗng';
  } else if (!/^\d+$/.test(phone)) {
    errors.phone = 'Số điện thoại chỉ được chứa số';
  } else if (phone.length < 9 || phone.length > 11) {
    errors.phone = 'Số điện thoại phải có độ dài từ 9 đến 11 ký tự';
  }

  if (email && !email.includes('@')) {
    errors.email = 'Email phải có ký tự @';
  }

  if (!course) {
    errors.course = 'Khóa học quan tâm không được rỗng';
  }

  return {
    isValid: Object.keys(errors).length === 0,
    errors,
  };
}

export function createCustomerPayload(formData) {
  return {
    fullName: normalizeText(formData.fullName),
    phone: normalizeText(formData.phone),
    email: normalizeText(formData.email),
    course: normalizeText(formData.course),
    status: CUSTOMER_STATUS.NEW,
    isFavorite: false,
    note: normalizeText(formData.note),
  };
}

export function createUpdateCustomerPayload(formData, id) {
  return {
    id: String(id),
    fullName: normalizeText(formData.fullName),
    phone: normalizeText(formData.phone),
    email: normalizeText(formData.email),
    course: normalizeText(formData.course),
    status: normalizeText(formData.status) || CUSTOMER_STATUS.NEW,
    isFavorite: Boolean(formData.isFavorite),
    note: normalizeText(formData.note),
  };
}

export function filterCustomers(customers, filterType = 'all') {
  const list = Array.isArray(customers) ? customers : [];

  if (filterType === 'all') return list;
  if (filterType === 'favorite') return list.filter((customer) => customer.isFavorite === true);

  return list.filter((customer) => customer.status === filterType);
}

export function searchCustomers(customers, keyword = '') {
  const list = Array.isArray(customers) ? customers : [];
  const q = normalizeText(keyword).toLowerCase();

  if (!q) return list;

  return list.filter((customer) => {
    const searchableText = [
      customer.fullName,
      customer.phone,
      customer.email,
      customer.course,
    ]
      .map((value) => String(value ?? '').toLowerCase())
      .join(' ');

    return searchableText.includes(q);
  });
}

export function updateCustomerStatusInList(customers, id, status) {
  const targetId = String(id);

  return customers.map((customer) => {
    if (String(customer.id) !== targetId) return customer;

    return {
      ...customer,
      status,
    };
  });
}

export function updateCustomerInList(customers, updatedCustomer) {
  const targetId = String(updatedCustomer.id);

  return customers.map((customer) => {
    if (String(customer.id) !== targetId) return customer;
    return { ...updatedCustomer };
  });
}

export function removeCustomerFromList(customers, id) {
  const targetId = String(id);
  return customers.filter((customer) => String(customer.id) !== targetId);
}

export function getVisibleCustomers(customers, filterType, keyword) {
  return searchCustomers(filterCustomers(customers, filterType), keyword);
}
