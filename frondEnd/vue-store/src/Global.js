exports.install = function (Vue) {
  Vue.prototype.$target = "http://127.0.0.1:8000/";
  Vue.prototype.notifySucceed = function (msg) {
    this.$notify({
      title: "Success",
      message: msg,
      type: "success",
      offset: 100
    });
  };
  Vue.prototype.notifyError = function (msg) {
    this.$notify.error({
      title: "Error",
      message: msg,
      offset: 100
    });
  };
}