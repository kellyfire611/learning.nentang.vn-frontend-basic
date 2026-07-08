function safeArray(value) {
  return Array.isArray(value) ? value : [];
}

function toDateKey(value) {
  if (!value) {
    return 'Không rõ ngày';
  }

  const date = new Date(value);

  if (Number.isNaN(date.getTime())) {
    return 'Không rõ ngày';
  }

  return date.toISOString().slice(0, 10);
}

export function calculateTotalRevenue(orders) {
  return safeArray(orders).reduce((sum, order) => sum + (Number(order?.totalAmount) || 0), 0);
}

export function countTotalOrders(orders) {
  return safeArray(orders).length;
}

export function calculateTotalSoldQuantity(orders) {
  return safeArray(orders).reduce((total, order) => {
    const items = safeArray(order?.items);
    const orderQuantity = items.reduce((sum, item) => sum + (Number(item?.quantity) || 0), 0);

    return total + orderQuantity;
  }, 0);
}

export function getBestSellingProduct(orders) {
  const quantityByProduct = new Map();

  safeArray(orders).forEach((order) => {
    safeArray(order?.items).forEach((item) => {
      if (!item?.productId) {
        return;
      }

      const current = quantityByProduct.get(item.productId) || {
        productId: item.productId,
        name: item.name || item.productId,
        quantity: 0
      };

      current.quantity += Number(item.quantity) || 0;
      quantityByProduct.set(item.productId, current);
    });
  });

  const products = [...quantityByProduct.values()];

  if (products.length === 0) {
    return null;
  }

  return products.sort((a, b) => b.quantity - a.quantity)[0];
}

export function getLowStockProducts(products, threshold = 5) {
  return safeArray(products).filter((product) => Number(product?.stock) <= threshold);
}

export function groupRevenueByDate(orders) {
  const revenueByDate = new Map();

  safeArray(orders).forEach((order) => {
    const dateKey = toDateKey(order?.createdAt);
    const currentRevenue = revenueByDate.get(dateKey) || 0;
    revenueByDate.set(dateKey, currentRevenue + (Number(order?.totalAmount) || 0));
  });

  return [...revenueByDate.entries()]
    .map(([date, revenue]) => ({ date, revenue }))
    .sort((a, b) => a.date.localeCompare(b.date));
}

export function groupSoldQuantityByProduct(orders) {
  const quantityByProduct = new Map();

  safeArray(orders).forEach((order) => {
    safeArray(order?.items).forEach((item) => {
      if (!item?.productId) {
        return;
      }

      const current = quantityByProduct.get(item.productId) || {
        productId: item.productId,
        name: item.name || item.productId,
        quantity: 0
      };

      current.quantity += Number(item.quantity) || 0;
      quantityByProduct.set(item.productId, current);
    });
  });

  return [...quantityByProduct.values()].sort((a, b) => b.quantity - a.quantity);
}
