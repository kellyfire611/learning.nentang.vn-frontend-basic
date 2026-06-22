import { describe, expect, it, vi } from 'vitest';

import {
  CUSTOMER_STATUS,
  createCustomerPayload,
  filterCustomers,
  updateCustomerStatusInList,
  validateCustomerForm,
} from '../../src/customerBusiness.js';

describe('customer flow - Given When Then', () => {
  it('Given danh sách có 3 khách hàng, When lọc registered, Then chỉ hiển thị khách hàng đã đăng ký', () => {
    const givenCustomers = [
      { id: '1', fullName: 'Nguyễn Văn An', status: CUSTOMER_STATUS.NEW },
      { id: '2', fullName: 'Trần Thị Bình', status: CUSTOMER_STATUS.CONTACTED },
      { id: '3', fullName: 'Lê Minh Cường', status: CUSTOMER_STATUS.REGISTERED },
    ];

    const result = filterCustomers(givenCustomers, CUSTOMER_STATUS.REGISTERED);

    expect(result).toHaveLength(1);
    expect(result[0].status).toBe(CUSTOMER_STATUS.REGISTERED);
    expect(result[0].fullName).toBe('Lê Minh Cường');
  });

  it('Given form có số điện thoại sai định dạng, When bấm thêm khách hàng, Then báo lỗi và không gọi API', async () => {
    const createCustomerApi = vi.fn();
    const formData = {
      fullName: 'Nguyễn Văn An',
      phone: '09abc1234',
      email: 'an@example.com',
      course: 'Lập trình Web',
      note: '',
    };

    const validation = validateCustomerForm(formData);

    if (validation.isValid) {
      await createCustomerApi(createCustomerPayload(formData));
    }

    expect(validation.isValid).toBe(false);
    expect(validation.errors.phone).toBe('Số điện thoại chỉ được chứa số');
    expect(createCustomerApi).not.toHaveBeenCalled();
  });

  it('Given danh sách có một khách mới, When cập nhật trạng thái contacted, Then khách hàng đó đã tư vấn', () => {
    const givenCustomers = [
      { id: '1', fullName: 'Nguyễn Văn An', status: CUSTOMER_STATUS.NEW },
    ];

    const result = updateCustomerStatusInList(givenCustomers, '1', CUSTOMER_STATUS.CONTACTED);

    expect(result[0].status).toBe(CUSTOMER_STATUS.CONTACTED);
  });
});
