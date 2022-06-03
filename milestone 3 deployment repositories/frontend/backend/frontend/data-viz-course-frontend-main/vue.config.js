const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    allowedHosts: "all"
  },
  configureWebpack: {
    resolve: {
      alias: {
      },
      fallback: {
        fs: false,
        path: false,
      }
    }
  }
})
