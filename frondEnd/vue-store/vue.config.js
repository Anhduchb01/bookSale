/*
 * @Description: 配置文件
 * @Author: hai-27
 * @Date: 2020-02-07 16:23:00
 * @LastEditors: hai-27
 * @LastEditTime: 2021-03-03 22:32:57
 */
module.exports = {
  publicPath: './',
  devServer: {
    open: true,
    proxy: {
      '/api': {
        target: 'http://localhost:3000/', 
        changeOrigin: true, 
        pathRewrite: {
          '^/api': ''
        }
      }
    }
  }
}