import { defineConfig } from 'vitest/config';

export default defineConfig({
  test: {
    // archive/ holds tools that were taken off the sites; keep their tests out of the run.
    exclude: ['**/node_modules/**', '**/dist/**', 'archive/**'],
  },
});
