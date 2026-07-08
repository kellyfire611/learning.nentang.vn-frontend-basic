import { describe, expect, it } from 'vitest';
import {
  addItemToCart,
  buildOrderFromCart,
  calculateCartTotal,
  calculateLineTotal,
  removeItemFromCart,
  validateQuantity
} from '../../src/services/cartService.js';

describe('cartService', () => {
  it('tính đúng thành tiền của một dòng sản phẩm', () => {
    expect(calculateLineTotal({ price: 25000, quantity: 2 })).toBe(50000);
  });

  it('tính đúng tổng tiền giỏ hàng', () => {
    const cartItems = [
      { price: 25000, quantity: 2 },
      { price: 10000, quantity: 3 }
    ];

    expect(calculateCartTotal(cartItems)).toBe(80000);
  });

  it('trả về 0 khi giỏ hàng không phải mảng', () => {
    expect(calculateCartTotal(null)).toBe(0);
  });

  it('không cho nhập số lượng nhỏ hơn hoặc bằng 0', () => {
    const product = { id: 'p01', stock: 10 };
    const result = validateQuantity(product, 0);

    expect(result.valid).toBe(false);
    expect(result.message).toBe('Số lượng phải là số nguyên lớn hơn 0');
  });

  it('không cho mua vượt tồn kho', () => {
    const product = { id: 'p01', stock: 5 };
    const result = validateQuantity(product, 10);

    expect(result.valid).toBe(false);
    expect(result.message).toBe('Không đủ hàng trong kho');
  });

  it('thêm sản phẩm mới vào giỏ hàng', () => {
    const product = {
      id: 'p01',
      code: 'TS01',
      name: 'Trà sữa',
      price: 25000,
      stock: 10
    };

    const result = addItemToCart([], product, 2);

    expect(result.success).toBe(true);
    expect(result.cartItems).toHaveLength(1);
    expect(result.cartItems[0].lineTotal).toBe(50000);
  });

  it('cộng dồn số lượng nếu sản phẩm đã có trong giỏ', () => {
    const product = {
      id: 'p01',
      code: 'TS01',
      name: 'Trà sữa',
      price: 25000,
      stock: 10
    };

    const cartItems = [
      {
        productId: 'p01',
        code: 'TS01',
        name: 'Trà sữa',
        price: 25000,
        quantity: 2,
        lineTotal: 50000
      }
    ];

    const result = addItemToCart(cartItems, product, 3);

    expect(result.success).toBe(true);
    expect(result.cartItems).toHaveLength(1);
    expect(result.cartItems[0].quantity).toBe(5);
    expect(result.cartItems[0].lineTotal).toBe(125000);
  });

  it('xóa sản phẩm khỏi giỏ hàng', () => {
    const cartItems = [
      { productId: 'p01', name: 'Trà sữa' },
      { productId: 'p02', name: 'Bánh mì' }
    ];

    const result = removeItemFromCart(cartItems, 'p01');

    expect(result).toEqual([{ productId: 'p02', name: 'Bánh mì' }]);
  });

  it('tạo object đơn hàng từ giỏ hàng', () => {
    const cartItems = [
      {
        productId: 'p01',
        code: 'TS01',
        name: 'Trà sữa',
        price: 25000,
        quantity: 2,
        lineTotal: 50000
      }
    ];

    const order = buildOrderFromCart(cartItems, {
      id: 'o-test',
      customerName: 'Khách lẻ',
      createdAt: '2026-07-06T00:00:00.000Z'
    });

    expect(order.id).toBe('o-test');
    expect(order.customerName).toBe('Khách lẻ');
    expect(order.totalAmount).toBe(50000);
    expect(order.items).toHaveLength(1);
  });
});
