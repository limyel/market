<template>
    <div id="header">
        <span @click="goBack"><</span>
        <p>{{title}}</p>
        <span></span>
    </div>
</template>

<script>
    export default {
        props: {
            title: {
                type: String,
                default: 'null'
            }
        },
        methods: {
            goBack: function() {
                this.$router.back();
            }
        }
    }
</script>

<style lang="stylus" scoped>
    #header
        display flex
        position fixed
        top 0
        left 0
        z-index 800
        width 100%
        padding 3% 3%
        font-size 1.3em
        background-color #e5e5e5
        span
            width 10%
        p
            width 72%
            text-align center
</style>