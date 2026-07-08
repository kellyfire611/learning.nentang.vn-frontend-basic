import { execFileSync } from 'node:child_process';
import { test, expect } from '@playwright/test';

test.beforeEach(async ({ page }) => {
  execFileSync('node', ['scripts/reset-db.mjs'], { cwd: process.cwd() });
  await page.goto('/index.html');
  await expect(page.getByTestId('product-list')).toContainText('Trà sữa');
});

test('hiển thị danh sách sản phẩm từ json-server', async ({ page }) => {
  await expect(page.getByTestId('product-row-p01')).toBeVisible();
  await expect(page.getByTestId('product-row-p01')).toContainText('Trà sữa');
  await expect(page.getByTestId('product-stock-p01')).toHaveText('10');
});

test('thêm sản phẩm vào giỏ hàng và tính tổng tiền', async ({ page }) => {
  await page.getByTestId('product-quantity-p01').fill('2');
  await page.getByTestId('add-to-cart-p01').click();

  await expect(page.getByTestId('cart-items')).toContainText('Trà sữa');
  await expect(page.getByTestId('cart-total')).toContainText('50.000');
});

test('không cho nhập số lượng nhỏ hơn hoặc bằng 0', async ({ page }) => {
  await page.getByTestId('product-quantity-p01').fill('0');
  await page.getByTestId('add-to-cart-p01').click();

  await expect(page.getByTestId('message')).toContainText('Số lượng phải là số nguyên lớn hơn 0');
});

test('không cho mua vượt tồn kho', async ({ page }) => {
  await page.getByTestId('product-quantity-p01').fill('99');
  await page.getByTestId('add-to-cart-p01').click();

  await expect(page.getByTestId('message')).toContainText('Không đủ hàng trong kho');
});

test('thanh toán thành công, lưu đơn hàng và trừ tồn kho', async ({ page }) => {
  await page.getByTestId('product-quantity-p01').fill('1');
  await page.getByTestId('add-to-cart-p01').click();
  await page.getByTestId('checkout-button').click();

  await expect(page.getByTestId('message')).toContainText('Thanh toán thành công và đã lưu đơn hàng');
  await expect(page.getByTestId('cart-items')).toContainText('Giỏ hàng đang rỗng');
  await expect(page.getByTestId('product-stock-p01')).toHaveText('9');
});

test('thanh toán khi giỏ hàng rỗng thì hiển thị lỗi', async ({ page }) => {
  await page.getByTestId('checkout-button').click();

  await expect(page.getByTestId('message')).toContainText('Giỏ hàng đang rỗng');
});
