import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
Vue.use(ElementUI);

import Global from './Global';
Vue.use(Global);

import Axios from 'axios';
Vue.prototype.$axios = Axios;

Axios.interceptors.request.use(
  config => {
    return config;
  },
  error => {

    router.push({ path: "/error" });
    return Promise.reject(error);
  }
);

Axios.interceptors.response.use(
  res => {
    if (res.data.code === "401") {

      Vue.prototype.notifyError(res.data.msg);
      store.dispatch("setShowLogin", true);
    }
    if (res.data.code === "500") {
      router.push({ path: "/error" });
    }
    return res;
  },
  error => {
    router.push({ path: "/error" });
    return Promise.reject(error);
  }
);
router.beforeResolve((to, from, next) => {
  const loginUser = store.state.user.user;
  if (to.meta.requireAuth) {
    if (!loginUser) {
      store.dispatch("setShowLogin", true);
      if (from.name == null) {
        next("/");
        return;
      }
      next(false);
      return;
    }
  }
  next();
});

Vue.filter('dateFormat', (dataStr) => {
  var time = new Date(dataStr);
  function timeAdd0 (str) {
    if (str < 10) {
      str = '0' + str;
    }
    return str;
  }
  var y = time.getFullYear();
  var m = time.getMonth() + 1;
  var d = time.getDate();
  var h = time.getHours();
  var mm = time.getMinutes();
  var s = time.getSeconds();
  return y + '-' + timeAdd0(m) + '-' + timeAdd0(d) + ' ' + timeAdd0(h) + ':' + timeAdd0(mm) + ':' + timeAdd0(s);
});

//全局组件
import MyMenu from './components/MyMenu';
Vue.component(MyMenu.name, MyMenu);
import MyList from './components/MyList';
Vue.component(MyList.name, MyList);
import MyLogin from './components/MyLogin';
Vue.component(MyLogin.name, MyLogin);
import MyRegister from './components/MyRegister';
Vue.component(MyRegister.name, MyRegister);

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
