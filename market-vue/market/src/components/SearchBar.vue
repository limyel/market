<template>
    <div id="search-bar">
        <div class="header">
            <i class="cubeic-location"></i>景苑花园 >
            <div class="notification"><i class="cubeic-notification" style="text-align: right"></i></div>
        </div>
        <div class="search">
            <p @click="toSearch"><i class="cubeic-search"></i>搜索</p>
        </div>
    </div>
</template>

<script>
    export default {
        props: {
        },
        data: function() {
            return {
            }
        },
        methods: {
            toSearch() {
                this.$router.push('/search');
            }
        },
        computed: {

        }
    }
</script>

<style>
    #search-bar {
        font-size: 1.2em;
        background-color: lightskyblue;
    }

    .header {
        padding: 5% 3% 3%;
    }

    .notification {
        float: right;
    }

    .search {
        padding-bottom: 3%;
        padding-top: 3%;
        padding-left: 6%;
        font-size: 0.9em;
        background-color: white;
        border-top-left-radius: 20px;
        border-top-right-radius: 20px;
    }

    #search-bar p {
        width: 90%;
        border-radius: 30px;
        background-color: darkgray;
        text-align: center;
        padding: 2%;

    }


</style>