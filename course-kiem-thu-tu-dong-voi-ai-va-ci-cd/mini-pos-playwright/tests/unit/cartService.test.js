import { describe, expect, test } from 'vitest';
import {
  calculateCartTotal,
  calculateLineTotal,
  updateStockAfterCheckout,
  validateQuantity
} from '../../src/services/cartService.js';

describe('validateQuantity', () => {
  test('số lượng hợp lệ', () => {
    const result = validateQuantity(2, 10);

    expect(result.valid).toBe(true);
    expect(result.message).toBe('');
  });

  test('số lượng bằng 0 là không hợp lệ', () => {
    const result = validateQuantity(0, 10);

    expect(result.valid).toBe(false);
    expect(result.message).toBe('Số lượng phải lớn hơn 0');
  });

  test('số lượng âm là không hợp lệ', () => {
    const result = validateQuantity(-1, 10);

    expect(result.valid).toBe(false);
    expect(result.message).toBe('Số lượng phải lớn hơn 0');
  });

  test('số lượng vượt tồn kho là không hợp lệ', () => {
    const result = validateQuantity(99, 10);

    expect(result.valid).toBe(false);
    expect(result.message).toBe('Số lượng vượt quá tồn kho');
  });
});

describe('calculateLineTotal', () => {
  test('tính đúng thành tiền một dòng', () => {
    expect(calculateLineTotal(25000, 3)).toBe(75000);
  });
});

describe('calculateCartTotal', () => {
  test('tính đúng tổng tiền nhiều sản phẩm', () => {
    const cartItems = [
      { id: '1', name: 'Trà sữa', price: 25000, quantity: 2 },
      { id: '2', name: 'Bánh mì', price: 15000, quantity: 3 }
    ];

    expect(calculateCartTotal(cartItems)).toBe(95000);
  });

  test('giỏ hàng rỗng thì tổng tiền bằng 0', () => {
    expect(calculateCartTotal([])).toBe(0);
  });
});

describe('updateStockAfterCheckout', () => {
  test('mua thành công thì tồn kho giảm đúng', () => {
    const products = [
      { id: '1', name: 'Trà sữa', stock: 10 },
      { id: '2', name: 'Bánh mì', stock: 5 }
    ];

    const cartItems = [
      { id: '1', name: 'Trà sữa', quantity: 3 }
    ];

    const updatedProducts = updateStockAfterCheckout(products, cartItems);

    expect(updatedProducts[0].stock).toBe(7);
    expect(updatedProducts[1].stock).toBe(5);
  });
});
