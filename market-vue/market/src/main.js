import Vue from 'vue'
import '../setAxios'
import axios from 'axios'
import Vuex from 'vuex'
import './cube-ui'
import App from './App.vue'
import router from './router'
import store from './store'

Vue.config.productionTip = false;
Vue.prototype.axios = axios;

router.beforeEach((to, from, next) => {
    store.commit('setToken',localStorage.getItem('token'));
    if(to.meta.requireAuth) {
        if(store.state.token) {
            next();
        } else {
            next({
                path: '/registerlogin',
                query: {redirect: to.fullPath}
            })
        }
    } else {
        next();
    }
});

new Vue({
    router,
    store,
    render: h => h(App)
}).$mount('#app')
