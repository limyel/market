<template>
    <div id="register-login">
        <h2>欢迎登录 market</h2>
        <div class="phone">
            <cube-input v-model="phone" type="text"></cube-input>
            <cube-input v-model="code" type="text" v-show="isGet"></cube-input>
        </div>
        <cube-button id="submit" @click="registerLogin">{{msg}}</cube-button>
    </div>
</template>

<script>
    export default {
        data: function() {
            return {
                phone: '',
                get: '获取短信验证码',
                send: '注册或登录',
                isGet: false,
                code: ''
            }
        },
        methods: {
            registerLogin: function() {
                if(this.isGet) {
                    this.axios.post('/api/users/registerlogin/', {"username": this.phone, "password": this.code}).then(res => {
                        console.log(res.data);
                        localStorage.setItem('token', res.data.token);
                        this.$store.commit('setToken', localStorage.getItem('token'));
                        this.axios.get('/api/users/').then(res => {
                            localStorage.setItem('username', res.data.username);
                            localStorage.setItem('picture', res.data.picture);
                            localStorage.setItem('phone', res.data.phone);
                            this.$store.commit('setPicture', localStorage.getItem('picture'));
                            this.$store.commit('setPhone', localStorage.getItem('phone'));
                            this.$store.commit('setUsername', localStorage.getItem('username'));
                        });
                        this.$router.back();
                    })
                } else {
                    console.log(this.phone);
                    this.axios.post('/api/users/getcode/', {"phone": this.phone});
                }
                this.isGet = !this.isGet;
            }
        },
        computed: {
            msg: function() {
                if(this.isGet) {
                    return this.send;
                } else {
                    return this.get;
                }
            }
        }

    }
</script>

<style lang="stylus" scoped>
    #register-login
        margin 30% 0
        padding 0 5%
        h2
            font-size 2em
            margin-bottom: 20%;
        .phone
            padding 0 5%
            margin 3% 0

</style>