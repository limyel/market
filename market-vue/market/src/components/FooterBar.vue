<template>
    <div id="footer-bar">
        <cube-tab-bar
                v-model="selectedLabelDefault"
                :data="tabs"
                @click="clickHandler"
                @change="changeHandler"
        >
        </cube-tab-bar>
    </div>
</template>

<script>
    export default {
        data () {
            return {
                selectedLabelDefault: '首页',
                tabs: [{
                    label: '首页',
                    icon: 'cubeic-home'
                }, {
                    label: '分类',
                    icon: 'cubeic-tag'
                }, {
                    label: '购物车',
                    icon: 'cubeic-mall'
                }, {
                    label: '我的',
                    icon: 'cubeic-person'
                }]
            }
        },
        methods: {
            clickHandler (label) {
                console.log(this.$route.path);
                switch(label) {
                    case '首页': this.$router.push('/index/choice');break;
                    case '分类': this.$router.push('/category');break;
                    case '购物车': this.$router.push('/cart');break;
                    case '我的': this.$router.push('/mine');
                }
            },
            changeHandler (label) {
                switch(label) {
                    case '首页': this.$router.push('/index/choice');break;
                    case '分类': this.$router.push('/category');break;
                    case '购物车': this.$router.push('/cart');break;
                    case '我的': this.$router.push('/mine');
                }
            }
        }
    }
</script>

<style>
    .cube-tab-bar {
        position: fixed;
        bottom: 0;
        left: 0 ;
        width: 100%;
        background-color: whitesmoke;
        border-top: 1px solid darkgray;
        font-size: 1em;
        z-index: 1000;
    }
</style>