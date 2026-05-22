import { describe, expect, it } from "vitest";
import { createCart } from "../../src/cart/cart.js";
import { products } from "../../src/data/products.js";

describe("cart business rules", () => {
  it("them cung mot san pham se cong don so luong", () => {
    const cart = createCart(products);

    cart.addItem(1);
    cart.addItem(1, 2);

    expect(cart.getState().items).toEqual([
      expect.objectContaining({ id: 1, quantity: 3 })
    ]);
  });

  it("tinh tong co phi ship khi don hang chua dat nguong", () => {
    const cart = createCart(products);

    cart.addItem(2);
    cart.addItem(3);

    expect(cart.getSummary()).toMatchObject({
      itemCount: 2,
      subtotal: 600000,
      discount: 0,
      shipping: 30000,
      total: 630000
    });
  });

  it("ap dung SAVE10 cho don hang hop le", () => {
    const cart = createCart(products);

    cart.addItem(1);
    cart.addItem(4);
    cart.setCoupon("save10");

    expect(cart.getSummary()).toMatchObject({
      appliedCoupon: "SAVE10",
      subtotal: 830000,
      discount: 83000,
      shipping: 30000,
      total: 777000
    });
  });

  it("COMBO15 can tu 3 san pham va tam tinh 1 trieu", () => {
    const cart = createCart(products);

    cart.addItem(1);
    cart.addItem(2);
    cart.addItem(4);
    cart.setCoupon("COMBO15");

    expect(cart.getSummary()).toMatchObject({
      appliedCoupon: "COMBO15",
      subtotal: 1150000,
      discount: 172500,
      shipping: 0,
      total: 977500
    });
  });

  it("cap nhat so luong san pham co anh huong den tong", () => {
    const cart = createCart(products);

    cart.addItem(3);
    cart.updateQuantity(3, 3);

    expect(cart.getSummary()).toMatchObject({
      itemCount: 3,
      subtotal: 840000,
      shipping: 0,
      total: 840000
    });
  });

  it("xoa san pham khoi gio se cap nhat state", () => {
    const cart = createCart(products);

    cart.addItem(1);
    cart.addItem(2);
    cart.removeItem(1);

    expect(cart.getState()).toMatchObject({
      items: [expect.objectContaining({ id: 2, quantity: 1 })],
      couponCode: ""
    });
  });

  it("throw khi cap nhat so luong cho san pham khong co trong gio", () => {
    const cart = createCart(products);
    expect(() => cart.updateQuantity(2, 1)).toThrow(/khong tim thay/i);
  });

  it("clear dat lai gio hang va coupon", () => {
    const cart = createCart(products);

    cart.addItem(1);
    cart.setCoupon("SAVE10");
    cart.clear();

    expect(cart.getState()).toMatchObject({
      items: [],
      couponCode: "",
      summary: expect.objectContaining({ total: 0, itemCount: 0 })
    });
  });

  it("khong cho them san pham khong ton tai", () => {
    const cart = createCart(products);
    expect(() => cart.addItem(99)).toThrow(/khong ton tai/i);
  });
});