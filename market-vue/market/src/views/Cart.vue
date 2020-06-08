<template>
    <div id="cart">
        <div class="location">
            <span><i class=" cubeic-location"></i>景苑花园></span>
        </div>
        <div class="goods">
            <div v-show="good_item.good_num > 0? true: false" v-for="(good_item, index) in get_items" class="good" :key="index">
                <p><img :src="good_item.good.images[0].image"></p>
                <p>{{good_item.good.name}}</p>
                <p class="good-add">
                    <span class="good-reduce cubeic-remove" v-show="true" @click="handleReduce(index)"></span>
                    <span class="good-num" :id="good_item.good.id" v-show="true">{{good_item.good_num}}</span>
                    <span class="good-add cubeic-add" @click="handleAdd(index)"></span>
                </p>
            </div>
        </div>
        <div class="addresses">
            <div :class="select === index? 'address active': 'address'" @click="choose(index)" v-for="(address, index) in addresses" :key="index">
                <p>{{address.name}}</p>
                <p>{{address.phone}}</p>
                <p>{{address.address}}</p>
            </div>
        </div>
        <input v-model="message" placeholder="备注" type="text"/>
        <cube-button @click="buy">结算&nbsp;&nbsp;{{mount}}</cube-button>
    </div>
</template>

<script>
    import Goods from "../components/Goods";

    export default {
        components: {
            Goods
        },
        data() {
            return {
                info: [],
                items: [],
                addresses: [],
                select_index: -1,
                message: ''
            }
        },
        methods: {
            handleAdd(index) {
                this.items[index].good_num += 1;
                let num = this.items[index].good_num;
                this.axios.post('/api/trades/shopping_carts/', {'good': good_id, 'good_num': num});
                document.getElementById(good_id).innerHTML = num;
            },
            handleReduce: function(index) {
                // let num = document.getElementById(good_id).innerHTML;
                // num = parseInt(num);
                this.items[index].good_num -= 1;
                let num = this.items[index].good_num;
                if(num === 0) {
                    this.axios.delete('/api/trades/shopping_carts/' + good_id + '/');
                    this.info = [];
                    this.items = [];
                    this.axios.get('/api/trades/shopping_carts/').then(res => {

                        this.info = res.data;
                        for(let i = 0; i < this.info.length; i++) {
                            let num = res.data[i].good_num;
                            this.axios.get('/api/goods/' + res.data[i].good + '/').then(res => {
                                this.items.push({good: res.data, good_num: num})
                            })
                        }
                    });
                }
                else
                    this.axios.post('/api/trades/shopping_carts/', {'good': good_id, 'good_num': num});
                document.getElementById(good_id).innerHTML = num;
            },
            choose(index) {
                this.select_index = index;
            },
            buy() {
                let addr = this.addresses[this.select_index];
                this.axios.post('/api/orders/', {remark: this.message, name: addr.name, phone: addr.phone, address: addr.address, mount: this.mount}).then(res => {
                    console.log(res.data);
                    window.location.href = res.data.alipay_url;
                })
            }
        },
        computed: {
            get_items() {
                return this.items;
            },
            goods() {
                return this.$store.cart;
            },
            select() {
                return this.select_index;
            },
            mount() {
                let mount = 0;
                for(let i = 0; i < this.items.length; i++) {
                    mount += this.items[i].good.discount * this.items[i].good_num;
                }
                return mount;
            }
        },
        mounted() {
            this.axios.get('/api/trades/shopping_carts/').then(res => {
                this.info = res.data;
                for(let i = 0; i < this.info.length; i++) {
                    let num = res.data[i].good_num;
                    this.axios.get('/api/goods/' + res.data[i].good + '/').then(res => {
                        // this.$store.commit('pushCart', {good: res.data, good_num: num});
                        this.items.push({good: res.data, good_num: num})
                    })
                }
            });
            this.axios.get('/api/user_operations/address/').then(res => {
                this.addresses = res.data;
            })
        }
    }
</script>

<style lang="stylus" scoped>
    .location
        position fixed
        top 0
        width 100%
        border-bottom 1px solid lightgray
        z-index 1000
        padding 3% 0
        font-size 1.2em
        text-align center

    .goods
        margin-top 15%
        .good
            display flex
            p
                width 33%;
            img
                width 50px
                height 50px

    .address
        font-size 1.2em
        padding-left 10%
        margin 5% 0
        line-height 150%

    .active
        background-color gray

    input
        line-height 30px
        width 80%
        margin-left 10%
        margin-bottom 10%
</style>