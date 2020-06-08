<template>
    <div id="order0">
        <Header :title="'待收货'"></Header>
        <div class="orders">
            <div class="order" v-for="(order, index) in getOrders" :key="index">
                <div class="goods">
                    <div class="good" v-for="(ordergood, index) in order.ordergood_set" :key="index">
                        <div><img :src="ordergood.good.images[0].image"/></div>
                        <div>{{ordergood.good.name}}</div>
                        <div>X {{ordergood.good_num}}</div>
                    </div>
                </div>
                <div class="info">
                </div>
                <cube-button @click="Ok(order.id)">确认收货</cube-button>
            </div>

        </div>
    </div>
</template>

<script>
    import Header from "../components/Header";

    export default {
        components: {
            Header
        },
        data() {
            return {
                orders: []
            }
        },
        mounted() {
            this.axios.get('/api/trades/order_0/').then(res => {
                this.orders = res.data;
            })
        },
        computed: {
            getOrders() {
                return this.orders;
            }
        },
        methods: {
            Ok(order_id) {
                this.axios.get('/api/trades/' + order_id + '/');
                this.axios.get('/api/trades/order_0/').then(res => {
                    this.orders = res.data;
                })
            }
        }
    }
</script>

<style lang="stylus" scoped>
    .orders
        margin-top 15%

    .order
        border-top 1px #4a4c5b solid
        border-bottom 1px #4a4c5b solid
        padding 3% 3%
        margin-bottom 8%

    .good
        display flex
        text-align center
        font-size 1.3em
        div
            width 30%
            img
                width 80%;
        margin-bottom 5%
</style>