<template>
    <div id="app">
        <router-view @isDisplay="isDisplay" class="page"></router-view>
        <FooterBar v-show="getDisplay"></FooterBar>
        <CartBar v-show="getNotDisplay"></CartBar>
    </div>

</template>

<script>
    import FooterBar from "./components/FooterBar";
    import CartBar from "./components/CartBar";

    export default {
        data: function() {
            return {
                display: true
            }
        },
        components: {
            FooterBar,
            CartBar
        },
        computed: {
            getDisplay: function() {
                return this.display;
            },
            getNotDisplay: function() {
                return !this.display;
            }
        },
        methods: {
            isDisplay: function() {
                this.display = !this.display;
            }
        }
    }

</script>

<style>
    #app {
    }
    .page {
        padding-bottom: 13%;
        /*height: 625px;*/
    }



</style>
