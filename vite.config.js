import { defineConfig } from 'vite';

// GitHub Pages serves a project site from /<repo>/, so asset URLs need that
// prefix. Locally (and on any host serving from the root) base stays '/'.
const base = process.env.DEPLOY_TARGET === 'gh-pages' ? '/crls-crew/' : '/';

export default defineConfig({
  base,
  build: {
    outDir: 'dist',
    assetsInlineLimit: 0,
    // Three.js is the bulk of this bundle and is needed for the hero, so
    // code-splitting it behind a dynamic import would only trade one wait for
    // another. 157 kB gzipped for a WebGL site is reasonable; the warning is
    // acknowledged rather than silenced by accident.
    chunkSizeWarningLimit: 700,
  },
});
