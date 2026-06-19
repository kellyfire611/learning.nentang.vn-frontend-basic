export const CUSTOMER_STATUS = {
  NEW: "new",
  CONTACTED: "contacted",
  REGISTERED: "registered",
};

export const CUSTOMER_FILTER = {
  ALL: "all",
  NEW: "new",
  CONTACTED: "contacted",
  REGISTERED: "registered",
  FAVORITE: "favorite",
};

export const CUSTOMER_STATUS_LABEL = {
  [CUSTOMER_STATUS.NEW]: "Khách mới",
  [CUSTOMER_STATUS.CONTACTED]: "Đã tư vấn",
  [CUSTOMER_STATUS.REGISTERED]: "Đã đăng ký",
};

function normalizeText(value) {
  return String(value ?? "").trim();
}

function normalizeKeyword(value) {
  return normalizeText(value).toLowerCase();
}

export function validateCustomerForm(customer) {
  const fullName = normalizeText(customer.fullName);
  const phone = normalizeText(customer.phone);
  const email = normalizeText(customer.email);
  const course = normalizeText(customer.course);
  const status = normalizeText(customer.status || CUSTOMER_STATUS.NEW);
  const errors = {};

  if (fullName.length === 0) {
    errors.fullName = "Vui lòng nhập họ tên khách hàng!";
  } else if (fullName.length < 3) {
    errors.fullName = "Họ tên phải có ít nhất 3 ký tự!";
  }

  if (phone.length === 0) {
    errors.phone = "Vui lòng nhập số điện thoại!";
  } else if (!/^\d+$/.test(phone)) {
    errors.phone = "Số điện thoại chỉ được chứa chữ số!";
  } else if (phone.length < 9 || phone.length > 11) {
    errors.phone = "Số điện thoại phải có từ 9 đến 11 chữ số!";
  }

  if (email.length > 0 && !email.includes("@")) {
    errors.email = "Email phải có ký tự @!";
  }

  if (course.length === 0) {
    errors.course = "Vui lòng nhập khóa học quan tâm!";
  }

  if (!Object.values(CUSTOMER_STATUS).includes(status)) {
    errors.status = "Trạng thái khách hàng không hợp lệ!";
  }

  return errors;
}

export function hasValidationErrors(errors) {
  return Object.keys(errors).length > 0;
}

export function getFirstValidationMessage(errors) {
  return Object.values(errors)[0] || "";
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

export function createCustomerUpdatePayload(formData) {
  return {
    fullName: normalizeText(formData.fullName),
    phone: normalizeText(formData.phone),
    email: normalizeText(formData.email),
    course: normalizeText(formData.course),
    status: normalizeText(formData.status || CUSTOMER_STATUS.NEW),
    isFavorite: Boolean(formData.isFavorite),
    note: normalizeText(formData.note),
  };
}

export function filterCustomers(customers, filter) {
  if (filter === CUSTOMER_FILTER.FAVORITE) {
    return customers.filter((customer) => customer.isFavorite === true);
  }

  if ([CUSTOMER_FILTER.NEW, CUSTOMER_FILTER.CONTACTED, CUSTOMER_FILTER.REGISTERED].includes(filter)) {
    return customers.filter((customer) => customer.status === filter);
  }

  return customers;
}

export function searchCustomers(customers, keyword) {
  const normalizedKeyword = normalizeKeyword(keyword);

  if (normalizedKeyword.length === 0) {
    return customers;
  }

  return customers.filter((customer) => {
    const searchableText = [customer.fullName, customer.phone, customer.email, customer.course]
      .map(normalizeKeyword)
      .join(" ");

    return searchableText.includes(normalizedKeyword);
  });
}

export function findCustomerById(customers, id) {
  return customers.find((customer) => String(customer.id) === String(id));
}

export function updateCustomerInList(customers, updatedCustomer) {
  return customers.map((customer) => {
    if (String(customer.id) === String(updatedCustomer.id)) {
      return updatedCustomer;
    }

    return customer;
  });
}

export function updateCustomerStatusInList(customers, id, status) {
  return customers.map((customer) => {
    if (String(customer.id) === String(id)) {
      return {
        ...customer,
        status,
      };
    }

    return customer;
  });
}

export function toggleCustomerFavoriteInList(customers, id, isFavorite) {
  return customers.map((customer) => {
    if (String(customer.id) === String(id)) {
      return {
        ...customer,
        isFavorite,
      };
    }

    return customer;
  });
}

export function removeCustomerFromList(customers, id) {
  return customers.filter((customer) => String(customer.id) !== String(id));
}

export function countCustomersByStatus(customers) {
  return {
    total: customers.length,
    new: customers.filter((customer) => customer.status === CUSTOMER_STATUS.NEW).length,
    contacted: customers.filter((customer) => customer.status === CUSTOMER_STATUS.CONTACTED).length,
    registered: customers.filter((customer) => customer.status === CUSTOMER_STATUS.REGISTERED).length,
    favorite: customers.filter((customer) => customer.isFavorite === true).length,
  };
}
