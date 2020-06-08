<template>
    <div id="favorite">
        <Header :title="'我的收藏'"></Header>
        <div class="favorites">
            <Goods :goods="goods"></Goods>
        </div>
    </div>
</template>

<script>
    import Header from "../components/Header";
    import Goods from "../components/Goods";

    export default {
        components: {
            Header,
            Goods
        },
        data() {
            return {
                goods: []
            }
        },
        created() {
            this.axios.get('/api/user_operations/').then(res => {
                this.goods = res.data;
            })
        }
    }
</script>

<style lang="stylus" scoped>
    #favorite
        padding 15%
</style>