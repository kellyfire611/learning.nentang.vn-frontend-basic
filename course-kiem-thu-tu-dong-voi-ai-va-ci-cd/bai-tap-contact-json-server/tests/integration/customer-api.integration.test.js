import { afterAll, beforeAll, describe, expect, it } from 'vitest';
import { spawn } from 'node:child_process';
import { copyFile, mkdtemp, rm } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import path from 'node:path';
import process from 'node:process';

import {
  createCustomer,
  deleteCustomer,
  fetchCustomers,
  patchCustomerStatus,
  setApiBaseUrl,
  updateCustomer,
} from '../../src/customerApiStore.js';

const port = 3101;
const baseUrl = `http://127.0.0.1:${port}`;
let serverProcess;
let tempDir;
let tempDbPath;

function jsonServerCliPath() {
  return path.join(process.cwd(), 'node_modules', 'json-server', 'lib', 'cli', 'bin.js');
}

async function waitForServer(url, timeoutMs = 10000) {
  const startedAt = Date.now();

  while (Date.now() - startedAt < timeoutMs) {
    try {
      const response = await fetch(url);
      if (response.ok) return;
    } catch {
      // Server chưa sẵn sàng.
    }

    await new Promise((resolve) => setTimeout(resolve, 250));
  }

  throw new Error(`JSON Server không khởi động sau ${timeoutMs}ms`);
}

async function createTempCustomer(overrides = {}) {
  return createCustomer({
    fullName: `Test User ${Date.now()}`,
    phone: `09${String(Date.now()).slice(-8)}`,
    email: 'test@example.com',
    course: 'Test API',
    status: 'new',
    isFavorite: false,
    note: 'Dữ liệu integration test',
    ...overrides,
  });
}

async function cleanupCustomer(id) {
  try {
    await deleteCustomer(id);
  } catch {
    // Có thể đã bị xóa trong test.
  }
}

beforeAll(async () => {
  tempDir = await mkdtemp(path.join(tmpdir(), 'customer-api-test-'));
  tempDbPath = path.join(tempDir, 'db.integration.json');
  await copyFile(path.join(process.cwd(), 'db.json'), tempDbPath);

  serverProcess = spawn(process.execPath, [jsonServerCliPath(), tempDbPath, '--port', String(port), '--host', '127.0.0.1'], {
    stdio: ['ignore', 'pipe', 'pipe'],
  });

  setApiBaseUrl(baseUrl);
  await waitForServer(`${baseUrl}/customers`);
}, 15000);

afterAll(async () => {
  if (serverProcess) serverProcess.kill();
  if (tempDir) await rm(tempDir, { recursive: true, force: true });
});

describe('Integration test với JSON Server thật', () => {
  it('TC-INT-001: GET /customers trả về mảng dữ liệu', async () => {
    const result = await fetchCustomers();

    expect(Array.isArray(result)).toBe(true);
    expect(result.length).toBeGreaterThan(0);
  });

  it('TC-INT-002: POST /customers thêm được khách hàng mới', async () => {
    const created = await createTempCustomer();

    try {
      expect(created.id).toBeDefined();
      expect(created.fullName).toContain('Test User');
    } finally {
      await cleanupCustomer(created.id);
    }
  });

  it('TC-INT-003: PATCH /customers/:id cập nhật được trạng thái', async () => {
    const created = await createTempCustomer();

    try {
      const updated = await patchCustomerStatus(created.id, 'contacted');

      expect(updated.status).toBe('contacted');
    } finally {
      await cleanupCustomer(created.id);
    }
  });

  it('TC-INT-004: PUT /customers/:id cập nhật đầy đủ thông tin', async () => {
    const created = await createTempCustomer();

    try {
      const payload = {
        ...created,
        fullName: 'Test User Updated',
        course: 'JavaScript nâng cao',
        status: 'registered',
        isFavorite: true,
      };

      const updated = await updateCustomer(created.id, payload);

      expect(updated.fullName).toBe('Test User Updated');
      expect(updated.course).toBe('JavaScript nâng cao');
      expect(updated.status).toBe('registered');
      expect(updated.isFavorite).toBe(true);
    } finally {
      await cleanupCustomer(created.id);
    }
  });

  it('TC-INT-005: DELETE /customers/:id xóa được dữ liệu', async () => {
    const created = await createTempCustomer();

    await deleteCustomer(created.id);

    const result = await fetch(`${baseUrl}/customers/${created.id}`);
    expect(result.status).toBe(404);
  });
});
