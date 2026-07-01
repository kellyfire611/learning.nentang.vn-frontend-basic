import { expect, test } from '@playwright/test';
import fs from 'node:fs';
import path from 'node:path';

function resetDatabase() {
  const rootDir = process.cwd();
  fs.copyFileSync(
    path.join(rootDir, 'db.seed.json'),
    path.join(rootDir, 'db.json')
  );
}

test.beforeEach(async ({ page }) => {
  resetDatabase();
  await page.goto('/');
});

test('hiển thị danh sách sản phẩm', async ({ page }) => {
  await expect(page.getByTestId('product-list')).toContainText('Trà sữa');
  await expect(page.getByTestId('product-list')).toContainText('Bánh mì');
  await expect(page.getByTestId('product-stock-1')).toHaveText('10');
});

test('thêm sản phẩm vào giỏ hàng', async ({ page }) => {
  await page.getByTestId('product-quantity-1').fill('2');
  await page.getByTestId('add-to-cart-1').click();

  await expect(page.getByTestId('message')).toContainText('Đã thêm sản phẩm vào giỏ hàng');
  await expect(page.getByTestId('cart-items')).toContainText('Trà sữa');
  await expect(page.getByTestId('cart-items')).toContainText('2 x 25.000');
  await expect(page.getByTestId('cart-total')).toContainText('50.000');
});

test('không cho nhập số lượng bằng 0', async ({ page }) => {
  await page.getByTestId('product-quantity-1').fill('0');
  await page.getByTestId('add-to-cart-1').click();

  await expect(page.getByTestId('message')).toContainText('Số lượng phải lớn hơn 0');
  await expect(page.getByTestId('cart-items')).toContainText('Giỏ hàng trống');
});

test('không cho mua vượt tồn kho', async ({ page }) => {
  await page.getByTestId('product-quantity-1').fill('99');
  await page.getByTestId('add-to-cart-1').click();

  await expect(page.getByTestId('message')).toContainText('Số lượng vượt quá tồn kho');
  await expect(page.getByTestId('cart-items')).toContainText('Giỏ hàng trống');
  await expect(page.getByTestId('product-stock-1')).toHaveText('10');
});

test('thanh toán thành công thì tồn kho giảm', async ({ page }) => {
  await expect(page.getByTestId('product-stock-1')).toHaveText('10');

  await page.getByTestId('product-quantity-1').fill('3');
  await page.getByTestId('add-to-cart-1').click();

  await page.getByTestId('checkout-button').click();

  await expect(page.getByTestId('message')).toContainText('Thanh toán thành công');
  await expect(page.getByTestId('product-stock-1')).toHaveText('7');
});

test('thanh toán xong thì giỏ hàng rỗng', async ({ page }) => {
  await page.getByTestId('product-quantity-1').fill('2');
  await page.getByTestId('add-to-cart-1').click();

  await expect(page.getByTestId('cart-items')).toContainText('Trà sữa');

  await page.getByTestId('checkout-button').click();

  await expect(page.getByTestId('cart-items')).toContainText('Giỏ hàng trống');
  await expect(page.getByTestId('cart-total')).toContainText('0');
});

test('giỏ hàng rỗng thì không cho thanh toán', async ({ page }) => {
  await page.getByTestId('checkout-button').click();

  await expect(page.getByTestId('message')).toContainText('Giỏ hàng đang rỗng');
});
