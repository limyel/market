<template>
    <div id="search">
        <Header :title="'搜索'"></Header>
        <div class="search">
            <input type="text" placeholder="搜索" v-model="keywords" @keyup.13="search"/>
            <Goods :goods="getGoods"></Goods>
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
                goods: [],
                keywords: ''
            }
        },
        computed: {
            getGoods() {
                return this.goods;
            }
        },
        methods: {
            search() {
                this.axios.get('/api/goods/' + this.keywords + '/').then(res => {
                    this.goods = res.data;
                })
            }
        }
    }
</script>

<style lang="stylus" scoped>
    .search
        margin-top 15%

    input
        line-height 30px
        width 80%
        margin-left 10%
</style>