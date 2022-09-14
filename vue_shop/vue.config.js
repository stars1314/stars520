// const { defineConfig } = require('@vue/cli-service')
// module.exports = defineConfig({
//   transpileDependencies: true
// })


// 跨域代理配置
module.exports = {
  devServer: {
    proxy: {
      '/': {
          target: 'http://localhost:5000',
          changeOrigin: true,
          ws: false,
          pathRewrite: {
            '^/': '/'
          }
      }
    }
  }
}