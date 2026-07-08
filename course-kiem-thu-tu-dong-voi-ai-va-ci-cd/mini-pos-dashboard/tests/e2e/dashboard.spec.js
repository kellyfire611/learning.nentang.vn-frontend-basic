import { execFileSync } from 'node:child_process';
import { test, expect } from '@playwright/test';

test.beforeEach(async () => {
  execFileSync('node', ['scripts/reset-db.mjs'], { cwd: process.cwd() });
});

test('mở dashboard và kiểm tra tiêu đề', async ({ page }) => {
  await page.goto('/dashboard.html');

  await expect(page.getByTestId('dashboard-title')).toHaveText('Dashboard báo cáo bán hàng');
});

test('dashboard hiển thị số liệu tổng quan', async ({ page }) => {
  await page.goto('/dashboard.html');

  await expect(page.getByTestId('total-revenue')).toContainText('225.000');
  await expect(page.getByTestId('total-orders')).toHaveText('3');
  await expect(page.getByTestId('total-sold-quantity')).toHaveText('13');
  await expect(page.getByTestId('best-selling-product')).toContainText('Mì ly');
});

test('dashboard hiển thị danh sách tồn kho thấp', async ({ page }) => {
  await page.goto('/dashboard.html');

  await expect(page.getByTestId('low-stock-list')).toContainText('Bánh mì');
  await expect(page.getByTestId('low-stock-list')).toContainText('Mì ly');
});

test('dashboard có đủ canvas biểu đồ', async ({ page }) => {
  await page.goto('/dashboard.html');

  await expect(page.getByTestId('revenue-chart')).toBeVisible();
  await expect(page.getByTestId('stock-chart')).toBeVisible();
  await expect(page.getByTestId('sold-quantity-chart')).toBeVisible();
});

test('luồng bán hàng làm dashboard cập nhật doanh thu và tổng đơn hàng', async ({ page }) => {
  await page.goto('/index.html');
  await expect(page.getByTestId('product-list')).toContainText('Trà sữa');

  await page.getByTestId('product-quantity-p01').fill('1');
  await page.getByTestId('add-to-cart-p01').click();
  await page.getByTestId('checkout-button').click();

  await expect(page.getByTestId('message')).toContainText('Thanh toán thành công và đã lưu đơn hàng');

  await page.goto('/dashboard.html');

  await expect(page.getByTestId('total-orders')).toHaveText('4');
  await expect(page.getByTestId('total-revenue')).toContainText('250.000');
});

test('luồng bán hàng làm tồn kho trên dashboard thay đổi', async ({ page }) => {
  await page.goto('/index.html');
  await expect(page.getByTestId('product-stock-p01')).toHaveText('10');

  await page.getByTestId('product-quantity-p01').fill('1');
  await page.getByTestId('add-to-cart-p01').click();
  await page.getByTestId('checkout-button').click();

  await page.goto('/dashboard.html');

  await expect(page.getByTestId('stock-chart')).toBeVisible();
  await expect(page.getByTestId('low-stock-list')).toContainText('Bánh mì');
});
