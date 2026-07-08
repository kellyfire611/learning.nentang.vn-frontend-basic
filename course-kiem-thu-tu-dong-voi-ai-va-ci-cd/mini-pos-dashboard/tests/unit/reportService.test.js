import { describe, expect, it } from 'vitest';
import {
  calculateTotalRevenue,
  calculateTotalSoldQuantity,
  countTotalOrders,
  getBestSellingProduct,
  getLowStockProducts,
  groupRevenueByDate,
  groupSoldQuantityByProduct
} from '../../src/services/reportService.js';

const sampleOrders = [
  {
    id: 'o001',
    totalAmount: 58000,
    createdAt: '2026-07-04T08:30:00.000Z',
    items: [
      { productId: 'p01', name: 'Trà sữa', quantity: 2 },
      { productId: 'p04', name: 'Nước suối', quantity: 1 }
    ]
  },
  {
    id: 'o002',
    totalAmount: 94000,
    createdAt: '2026-07-05T09:15:00.000Z',
    items: [
      { productId: 'p02', name: 'Bánh mì', quantity: 3 },
      { productId: 'p03', name: 'Cà phê sữa', quantity: 2 }
    ]
  },
  {
    id: 'o003',
    totalAmount: 73000,
    createdAt: '2026-07-05T10:45:00.000Z',
    items: [
      { productId: 'p01', name: 'Trà sữa', quantity: 1 },
      { productId: 'p05', name: 'Mì ly', quantity: 4 }
    ]
  }
];

describe('reportService', () => {
  it('tính đúng tổng doanh thu nhiều đơn hàng', () => {
    expect(calculateTotalRevenue(sampleOrders)).toBe(225000);
  });

  it('trả về 0 nếu danh sách đơn hàng rỗng khi tính doanh thu', () => {
    expect(calculateTotalRevenue([])).toBe(0);
  });

  it('đếm đúng số đơn hàng', () => {
    expect(countTotalOrders(sampleOrders)).toBe(3);
  });

  it('trả về 0 nếu mảng đơn hàng rỗng khi đếm đơn', () => {
    expect(countTotalOrders([])).toBe(0);
  });

  it('tính đúng tổng số lượng sản phẩm đã bán', () => {
    expect(calculateTotalSoldQuantity(sampleOrders)).toBe(13);
  });

  it('trả về 0 nếu không có đơn hàng khi tính số lượng bán', () => {
    expect(calculateTotalSoldQuantity([])).toBe(0);
  });

  it('tìm đúng sản phẩm bán chạy nhất', () => {
    const result = getBestSellingProduct(sampleOrders);

    expect(result).toEqual({
      productId: 'p05',
      name: 'Mì ly',
      quantity: 4
    });
  });

  it('trả về null nếu không có dữ liệu bán chạy', () => {
    expect(getBestSellingProduct([])).toBeNull();
  });

  it('lọc đúng sản phẩm có stock <= 5', () => {
    const products = [
      { id: 'p01', name: 'Trà sữa', stock: 10 },
      { id: 'p02', name: 'Bánh mì', stock: 4 },
      { id: 'p05', name: 'Mì ly', stock: 5 }
    ];

    expect(getLowStockProducts(products)).toEqual([
      { id: 'p02', name: 'Bánh mì', stock: 4 },
      { id: 'p05', name: 'Mì ly', stock: 5 }
    ]);
  });

  it('cho phép truyền threshold tùy chỉnh khi lọc tồn kho thấp', () => {
    const products = [
      { id: 'p01', name: 'Trà sữa', stock: 10 },
      { id: 'p02', name: 'Bánh mì', stock: 4 },
      { id: 'p05', name: 'Mì ly', stock: 8 }
    ];

    expect(getLowStockProducts(products, 8)).toHaveLength(2);
  });

  it('gom đúng doanh thu theo ngày và cộng nhiều đơn cùng ngày', () => {
    expect(groupRevenueByDate(sampleOrders)).toEqual([
      { date: '2026-07-04', revenue: 58000 },
      { date: '2026-07-05', revenue: 167000 }
    ]);
  });

  it('gom đúng số lượng bán theo sản phẩm và sắp xếp giảm dần', () => {
    expect(groupSoldQuantityByProduct(sampleOrders)).toEqual([
      { productId: 'p05', name: 'Mì ly', quantity: 4 },
      { productId: 'p01', name: 'Trà sữa', quantity: 3 },
      { productId: 'p02', name: 'Bánh mì', quantity: 3 },
      { productId: 'p03', name: 'Cà phê sữa', quantity: 2 },
      { productId: 'p04', name: 'Nước suối', quantity: 1 }
    ]);
  });
});
