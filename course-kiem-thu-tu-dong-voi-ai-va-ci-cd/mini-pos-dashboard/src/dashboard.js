import { getProducts } from './services/productApi.js';
import { getOrders } from './services/orderApi.js';
import {
  calculateTotalRevenue,
  calculateTotalSoldQuantity,
  countTotalOrders,
  getBestSellingProduct,
  getLowStockProducts,
  groupRevenueByDate,
  groupSoldQuantityByProduct
} from './services/reportService.js';
import { formatMoney } from './utils/formatMoney.js';

const messageElement = document.querySelector('[data-testid="dashboard-message"]');
const totalRevenueElement = document.querySelector('[data-testid="total-revenue"]');
const totalOrdersElement = document.querySelector('[data-testid="total-orders"]');
const totalSoldQuantityElement = document.querySelector('[data-testid="total-sold-quantity"]');
const bestSellingProductElement = document.querySelector('[data-testid="best-selling-product"]');
const lowStockListElement = document.querySelector('[data-testid="low-stock-list"]');

let revenueChartInstance = null;
let stockChartInstance = null;
let soldQuantityChartInstance = null;

function showMessage(message, type = 'info') {
  messageElement.textContent = message;
  messageElement.className = `message is-${type}`;
}

function clearMessage() {
  messageElement.textContent = '';
  messageElement.className = 'message';
}

function renderSummary(orders) {
  const totalRevenue = calculateTotalRevenue(orders);
  const totalOrders = countTotalOrders(orders);
  const totalSoldQuantity = calculateTotalSoldQuantity(orders);
  const bestSellingProduct = getBestSellingProduct(orders);

  totalRevenueElement.textContent = formatMoney(totalRevenue);
  totalOrdersElement.textContent = String(totalOrders);
  totalSoldQuantityElement.textContent = String(totalSoldQuantity);
  bestSellingProductElement.textContent = bestSellingProduct
    ? `${bestSellingProduct.name} (${bestSellingProduct.quantity})`
    : 'Chưa có dữ liệu';
}

function renderLowStockProducts(products) {
  const lowStockProducts = getLowStockProducts(products);

  if (!lowStockProducts.length) {
    lowStockListElement.innerHTML = '<li>Không có sản phẩm sắp hết hàng.</li>';
    return;
  }

  lowStockListElement.innerHTML = lowStockProducts
    .map(
      (product) => `
        <li>
          <strong>${product.name}</strong>
          <div>Mã: ${product.code}</div>
          <div class="warning-text">Còn lại: ${product.stock}</div>
        </li>
      `
    )
    .join('');
}

function destroyChart(chartInstance) {
  if (chartInstance) {
    chartInstance.destroy();
  }
}

function createBarChart(canvasId, labels, values, label) {
  const canvas = document.getElementById(canvasId);

  if (!canvas || typeof Chart === 'undefined') {
    return null;
  }

  return new Chart(canvas, {
    type: 'bar',
    data: {
      labels,
      datasets: [
        {
          label,
          data: values,
          borderWidth: 1
        }
      ]
    },
    options: {
      responsive: true,
      maintainAspectRatio: true,
      scales: {
        y: {
          beginAtZero: true
        }
      },
      plugins: {
        legend: {
          display: true
        }
      }
    }
  });
}

function renderCharts(products, orders) {
  destroyChart(revenueChartInstance);
  destroyChart(stockChartInstance);
  destroyChart(soldQuantityChartInstance);

  const revenueByDate = groupRevenueByDate(orders);
  const soldQuantityByProduct = groupSoldQuantityByProduct(orders);

  revenueChartInstance = createBarChart(
    'revenue-chart',
    revenueByDate.map((item) => item.date),
    revenueByDate.map((item) => item.revenue),
    'Doanh thu'
  );

  stockChartInstance = createBarChart(
    'stock-chart',
    products.map((product) => product.name),
    products.map((product) => product.stock),
    'Tồn kho'
  );

  soldQuantityChartInstance = createBarChart(
    'sold-quantity-chart',
    soldQuantityByProduct.map((item) => item.name),
    soldQuantityByProduct.map((item) => item.quantity),
    'Số lượng bán'
  );
}

async function loadDashboard() {
  clearMessage();

  try {
    const [products, orders] = await Promise.all([getProducts(), getOrders()]);

    renderSummary(orders);
    renderLowStockProducts(products);
    renderCharts(products, orders);

    if (!orders.length) {
      showMessage('Chưa có đơn hàng. Hãy quay về trang bán hàng để tạo đơn đầu tiên.', 'info');
    }
  } catch (error) {
    showMessage(error.message || 'Không thể tải dữ liệu dashboard', 'error');
  }
}

document.addEventListener('DOMContentLoaded', loadDashboard);
