import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';

import {
  createCustomer,
  deleteCustomer,
  fetchCustomers,
  patchCustomerStatus,
  setApiBaseUrl,
  updateCustomer,
} from '../../src/customerApiStore.js';

function createMockResponse(body, ok = true, status = 200) {
  return {
    ok,
    status,
    text: vi.fn().mockResolvedValue(body === undefined ? '' : JSON.stringify(body)),
    json: vi.fn().mockResolvedValue(body),
  };
}

const sampleCustomer = {
  fullName: 'Nguyễn Văn An',
  phone: '0912345678',
  email: 'an@example.com',
  course: 'Lập trình Web',
  status: 'new',
  isFavorite: false,
  note: 'Muốn học buổi tối',
};

describe('customerApiStore', () => {
  beforeEach(() => {
    setApiBaseUrl('http://localhost:3001');
    globalThis.fetch = vi.fn();
  });

  afterEach(() => {
    vi.restoreAllMocks();
  });

  it('TC-API-001: fetchCustomers gọi đúng GET /customers', async () => {
    fetch.mockResolvedValueOnce(createMockResponse([sampleCustomer]));

    const result = await fetchCustomers();

    expect(fetch).toHaveBeenCalledWith('http://localhost:3001/customers', expect.objectContaining({ method: 'GET' }));
    expect(result).toEqual([sampleCustomer]);
  });

  it('TC-API-002: createCustomer gọi đúng POST và gửi JSON body', async () => {
    fetch.mockResolvedValueOnce(createMockResponse({ id: '4', ...sampleCustomer }));

    await createCustomer(sampleCustomer);

    expect(fetch).toHaveBeenCalledWith(
      'http://localhost:3001/customers',
      expect.objectContaining({
        method: 'POST',
        body: JSON.stringify(sampleCustomer),
        headers: expect.objectContaining({ 'Content-Type': 'application/json' }),
      }),
    );
  });

  it('TC-API-003: patchCustomerStatus gọi đúng PATCH /customers/:id', async () => {
    fetch.mockResolvedValueOnce(createMockResponse({ id: '1', status: 'contacted' }));

    await patchCustomerStatus('1', 'contacted');

    expect(fetch).toHaveBeenCalledWith(
      'http://localhost:3001/customers/1',
      expect.objectContaining({
        method: 'PATCH',
        body: JSON.stringify({ status: 'contacted' }),
      }),
    );
  });

  it('TC-API-004: updateCustomer gọi đúng PUT /customers/:id', async () => {
    fetch.mockResolvedValueOnce(createMockResponse({ id: '1', ...sampleCustomer }));

    await updateCustomer('1', { id: '1', ...sampleCustomer });

    expect(fetch).toHaveBeenCalledWith(
      'http://localhost:3001/customers/1',
      expect.objectContaining({
        method: 'PUT',
        body: JSON.stringify({ id: '1', ...sampleCustomer }),
      }),
    );
  });

  it('TC-API-005: deleteCustomer gọi đúng DELETE /customers/:id', async () => {
    fetch.mockResolvedValueOnce(createMockResponse({}));

    await deleteCustomer('1');

    expect(fetch).toHaveBeenCalledWith(
      'http://localhost:3001/customers/1',
      expect.objectContaining({ method: 'DELETE' }),
    );
  });

  it('TC-API-006: API trả lỗi thì throw Error', async () => {
    fetch.mockResolvedValueOnce(createMockResponse({ message: 'Server lỗi' }, false, 500));

    await expect(fetchCustomers()).rejects.toThrow('Server lỗi');
  });
});
