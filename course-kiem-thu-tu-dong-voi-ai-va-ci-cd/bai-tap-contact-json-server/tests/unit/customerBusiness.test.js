import { describe, expect, it } from 'vitest';

import {
  createCustomerPayload,
  filterCustomers,
  removeCustomerFromList,
  searchCustomers,
  updateCustomerStatusInList,
  validateCustomerForm,
} from '../../src/customerBusiness.js';

const validForm = {
  fullName: 'Nguyễn Văn An',
  phone: '0912345678',
  email: 'an@example.com',
  course: 'Lập trình Web',
  note: 'Muốn học buổi tối',
};

const customers = [
  {
    id: '1',
    fullName: 'Nguyễn Văn An',
    phone: '0912345678',
    email: 'an@example.com',
    course: 'Lập trình Web',
    status: 'new',
    isFavorite: false,
    note: '',
  },
  {
    id: '2',
    fullName: 'Trần Thị Bình',
    phone: '0987654321',
    email: 'binh@example.com',
    course: 'Kiểm thử phần mềm',
    status: 'contacted',
    isFavorite: true,
    note: '',
  },
  {
    id: '3',
    fullName: 'Lê Minh Cường',
    phone: '0909123456',
    email: '',
    course: 'JavaScript cơ bản',
    status: 'registered',
    isFavorite: false,
    note: '',
  },
];

describe('customerBusiness', () => {
  it('TC-BUS-001: Họ tên rỗng thì báo lỗi', () => {
    const result = validateCustomerForm({ ...validForm, fullName: '   ' });

    expect(result.isValid).toBe(false);
    expect(result.errors.fullName).toBe('Họ tên không được rỗng');
  });

  it('TC-BUS-002: Họ tên dưới 3 ký tự thì báo lỗi', () => {
    const result = validateCustomerForm({ ...validForm, fullName: 'An' });

    expect(result.isValid).toBe(false);
    expect(result.errors.fullName).toBe('Họ tên phải có tối thiểu 3 ký tự');
  });

  it('TC-BUS-003: Số điện thoại chứa chữ thì báo lỗi', () => {
    const result = validateCustomerForm({ ...validForm, phone: '09abc1234' });

    expect(result.isValid).toBe(false);
    expect(result.errors.phone).toBe('Số điện thoại chỉ được chứa số');
  });

  it('TC-BUS-004: Email không có @ thì báo lỗi', () => {
    const result = validateCustomerForm({ ...validForm, email: 'anexample.com' });

    expect(result.isValid).toBe(false);
    expect(result.errors.email).toBe('Email phải có ký tự @');
  });

  it('TC-BUS-005: Tạo payload khách hàng mới đúng mặc định status = new và isFavorite = false', () => {
    const payload = createCustomerPayload({
      fullName: '  Nguyễn Văn An  ',
      phone: ' 0912345678 ',
      email: ' an@example.com ',
      course: ' Lập trình Web ',
      note: ' Muốn học buổi tối ',
    });

    expect(payload).toEqual({
      fullName: 'Nguyễn Văn An',
      phone: '0912345678',
      email: 'an@example.com',
      course: 'Lập trình Web',
      status: 'new',
      isFavorite: false,
      note: 'Muốn học buổi tối',
    });
  });

  it('TC-BUS-006: Lọc khách hàng status = contacted', () => {
    const result = filterCustomers(customers, 'contacted');

    expect(result).toHaveLength(1);
    expect(result[0].fullName).toBe('Trần Thị Bình');
  });

  it('TC-BUS-007: Tìm kiếm theo số điện thoại', () => {
    const result = searchCustomers(customers, '0909');

    expect(result).toHaveLength(1);
    expect(result[0].fullName).toBe('Lê Minh Cường');
  });

  it('TC-BUS-008: Cập nhật trạng thái khách hàng trong danh sách', () => {
    const result = updateCustomerStatusInList(customers, '1', 'contacted');

    expect(result.find((customer) => customer.id === '1').status).toBe('contacted');
    expect(customers.find((customer) => customer.id === '1').status).toBe('new');
  });

  it('TC-BUS-009: Xóa khách hàng khỏi danh sách', () => {
    const result = removeCustomerFromList(customers, '2');

    expect(result).toHaveLength(2);
    expect(result.some((customer) => customer.id === '2')).toBe(false);
  });
});
