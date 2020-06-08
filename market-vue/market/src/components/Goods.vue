<template>
    <div>
        <div class="goods">
            <div class="good" v-for="(good, good_index) in goods" :key="good_index">
                <div class="good-image">
                    <router-link :to="{name: 'Detail', params: {id: good.id}}"><img :src="good.images[0].image"/></router-link>
                </div>
                <div class="good-info">
                    <div class="good-desc">
                        <p class="good-name">{{good.name}}</p>
                        <p class="good-short">{{good.short}}</p>
                    </div>
                    <div class="good-check">
                        <div class="good-price">
                            <span class="good-newprice">{{good.discount}}&nbsp;&nbsp;</span>
                            <span class="good-oldprice">{{good.price}}</span>
                        </div>
                        <div class="good-add">
                            <span class="good-reduce cubeic-remove" v-show="true" @click="handleReduce(good.id)"></span>
                            <span class="good-num" :id="good.id" v-show="true">0</span>
                            <span class="good-add cubeic-add" @click="handleAdd(good.id)"></span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

</template>

<script>
    export default {
        props: {
            goods: Array
        },
        methods: {
            handleAdd: function(good_id) {
                let num = document.getElementById(good_id).innerHTML;
                num = parseInt(num);
                num += 1;
                this.axios.post('/api/trades/shopping_carts/', {'good': good_id, 'good_num': num});
                document.getElementById(good_id).innerHTML = num;
            },
            handleReduce: function(good_id) {
                let num = document.getElementById(good_id).innerHTML;
                num = parseInt(num);
                num -= 1;
                if(num == 0)
                    this.axios.delete('/api/trades/shopping_carts/' + good_id + '/');
                else
                    this.axios.post('/api/trades/shopping_carts/', {'good': good_id, 'good_num': num});
                document.getElementById(good_id).innerHTML = num;
            }
        },
        computed: {

        }
    }
</script>

<style>
    .goods {
        margin-top: 5%;
        width: 95%;
        padding-left: 5%;
    }
    .goods-image img {
        width: 100%;
        object-fit: cover;
    }

    .good {
        border-bottom: 1px solid lightgray;
        display: flex;
        margin-top: 5%;
        padding-bottom: 2%;
        width: 90%;
    }
    .good-image {
        width: 30%;
    }
    .good-image img {
        width: 100%;
        height: 100%;
    }
    .good-info {
        position: relative;
        width: 70%;
    }
    .good-name {
        font-size: 1.2em;
        font-weight: 500;
        margin-bottom: 5%;
    }
    .good-check {
        position: absolute;
        bottom: 0;
        display: flex;
        width: 100%;
        font-size: 1.3em;
    }
    .good-price {
        width: 70%;
    }
    .good-oldprice {
        font-size: 0.8em;
        color: gray;
        text-decoration: line-through;
    }
    .good-newprice {
        color: orange;
    }
    .good-add {
        width: 40%;
        text-align: right;
        color: gray;
    }
</style>