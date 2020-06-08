import Vue from 'vue'
import axios from "axios";
import router from "./src/router";
import store from "./src/store"

axios.interceptors.request.use(config => {
    if(store.state.token) {
        config.headers.Authorization = 'JWT ' + store.state.token;
    }
    console.log(config.headers.Authorization);
    return config;
});