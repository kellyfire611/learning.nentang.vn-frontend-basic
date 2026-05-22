import { defineConfig } from "@playwright/test";

export default defineConfig({
  testDir: "./tests/e2e",
  fullyParallel: true,
  use: {
    baseURL: "http://127.0.0.1:3108",
    headless: true
  },
  webServer: {
    command: "npm run serve",
    port: 3108,
    reuseExistingServer: false,
    stdout: "ignore",
    stderr: "pipe"
  }
});