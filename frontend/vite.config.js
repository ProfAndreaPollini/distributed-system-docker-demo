import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'

// https://vitejs.dev/config/
export default defineConfig({
  server: {
    port:9876,
    watch: {
      usePolling: true,
    },
    host: "0.0.0.0"
  },
  plugins: [svelte()],
})
