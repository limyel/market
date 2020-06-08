<template>
    <div id="mime">
        <div class="user-info">
            <img class="picture" :src="picture"/>
            <div class="user-phone">
                <p>{{username}}</p>
                <p>{{phone}}</p>
            </div>
        </div>
        <div class="operations">
            <p>&nbsp;&nbsp;&nbsp;<router-link :to="{name: 'Order0'}">待收货</router-link></p>
            <p>&nbsp;&nbsp;&nbsp;<router-link :to="{name: 'Order1'}">已完成</router-link></p>
            <p>&nbsp;&nbsp;&nbsp;<router-link :to="{name: 'Favorite'}">我的收藏</router-link></p>
            <p>&nbsp;&nbsp;&nbsp;<router-link :to="{name: 'Address'}">我的地址</router-link></p>
        </div>
        <cube-button @click="logout">退出登录</cube-button>
    </div>
</template>

<script>
    export default {
        data: function() {
            return {

            }
        },
        methods: {
            logout() {
                this.$store.commit('setToken', '');
                this.$store.commit('setUsername', '');
                this.$store.commit('setPhone', '');
                this.$store.commit('setPicture', '');
                localStorage.removeItem('token');
                localStorage.removeItem('username');
                localStorage.removeItem('phone');
                localStorage.removeItem('picture');
                this.$router.push('/index/choice');
            }
        },
        computed: {
            picture() {
                return localStorage.getItem('picture');
            },
            username() {
                return localStorage.getItem('username');
            },
            phone() {
                return localStorage.getItem('phone')
            }
        },
        mounted() {
            console.log(this.$store.state.picture)
        }
    }
</script>

<style lang="stylus" scoped>
    #mime
        background-color #e5e5e5

    .user-info
        background-color: lightskyblue;
        border-bottom-right-radius 30px
        border-bottom-left-radius 30px
        display flex
        padding 5% 5%
        .picture
            border-radius 80px
            width 35%
        .user-phone
            padding-left 10%
            padding-top 5%
            font-size 1.5em
            p
                margin-bottom 5%

    .operations
        padding 0 5%
        p
            line-height 400%
            font-size 1.3em
            border-top 1px solid gray

</style>