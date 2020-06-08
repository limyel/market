import Vue from 'vue'
import VueRouter from 'vue-router'

import Index from '../views/Index.vue'


Vue.use(VueRouter);

const routes = [
    {
        path: '/',
        redirect: '/index/choice'
    },
    {
        path: '/index',
        name: 'Index',
        component: () => import('../views/Index.vue'),
        children: [
            {
                path: 'choice',
                name: 'Choice',
                component: () => import('../views/Choice.vue')
            },
            {
                path: 'rush',
                name: 'Rush',
                component: () => import('../views/Rush.vue')
            },
            {
                path: 'discount',
                name: 'Discount',
                component: () => import('../views/Discount.vue')
            },
            {
                path: 'new',
                name: 'New',
                component: () => import('../views/New.vue')
            }
        ]
    },
    {
        path: '/category',
        name: 'Category',
        component: () => import('../views/Category.vue')
    },
    {
        path: '/cart',
        name: 'Cart',
        meta:{
            requireAuth: true,
        },
        component: () => import('../views/Cart.vue')
    },
    {
        path: '/mine',
        name: 'Mine',
        meta:{
            requireAuth: true,
        },
        component: () => import('../views/Mine.vue'),
    },
    {
        path: '/favorite',
        name: 'Favorite',
        component: () => import('../views/Favorite.vue'),
        meta:{
            requireAuth: true,
        },
    },
    {
        path: '/registerlogin',
        name: 'RegisterLogin',
        component: () => import('../views/RegisterLogin.vue')
    },
    {
        path: '/detail/:id',
        name: 'Detail',
        component: () => import('../views/Detail.vue')
    },
    {
        path: '/location',
        name: 'Location',
        component: () => import('../views/Location.vue')
    },
    {
        path: '/order0',
        name: 'Order0',
        component: () => import('../views/Order0.vue')
    },
    {
        path: '/order1',
        name: 'Order1',
        component: () => import('../views/Order1.vue')
    },
    {
        path: '/address',
        name: 'Address',
        component: () => import('../views/Address.vue')
    },
    {
        path: '/search',
        name: 'Search',
        component: () => import('../views/Search.vue')
    }

];

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
});

export default router
