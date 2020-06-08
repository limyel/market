<template>
    <div id="order1">
        <Header :title="'已完成'"></Header>
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
                    {{order.name}}<br/>
                    {{order.phone}}<br/>
                    {{order.address}}
                </div>
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
            this.axios.get('/api/trades/order_1/').then(res => {
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
                this.axios.get('/api/trades/order_1/').then(res => {
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

    .info
        font-size 1.2em
        padding-left 10%
        margin 2% 0
        line-height 150%
</style>