import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  testDir: './tests/e2e',
  timeout: 30_000,
  expect: {
    timeout: 5_000
  },
  fullyParallel: false,
  reporter: [['html'], ['list']],
  use: {
    baseURL: 'http://127.0.0.1:5173',
    trace: 'on-first-retry',
    screenshot: 'only-on-failure',
    video: 'retain-on-failure'
  },
  projects: [
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'] }
    }
  ],
  webServer: [
    {
      command: 'npm run api',
      url: 'http://127.0.0.1:3000/products',
      reuseExistingServer: !process.env.CI,
      timeout: 30_000
    },
    {
      command: 'npm run dev',
      url: 'http://127.0.0.1:5173/index.html',
      reuseExistingServer: !process.env.CI,
      timeout: 30_000
    }
  ]
});
