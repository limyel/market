import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        slides: [],
        categories: [],
        token: '',
        location: '',
        picture: '',
        phone: '',
        username: '',
        cart: []
    },
    mutations: {
        setSlides: function(state, slides) {
            state.slides = slides;
        },
        setCategories: function(state, categories) {
            state.categories = categories;
        },
        setToken: function(state, token) {
            state.token = token;
        },
        setLocation: function(state, location) {
            state.location = location;
            console.log(state.location);
        },
        setPicture: function(state, picture) {
            state.picture = picture;
        },
        setPhone: function(state, phone) {
            state.phone = phone;
        },
        setUsername: function(state, username) {
            state.username = username;
        },
        pushCart: function(state, cart) {
            state.cart.push(cart);
        }
    },
    actions: {
    },
    modules: {
    }
})
