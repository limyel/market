<template>
    <div id="choice">
        <div v-for="(item, item_index) in items" :key="item_index">
            <div class="goods-image">
                <img :src="item.image"/>
            </div>
            <div class="goods" v-for="(good, good_index) in item.goods" :key="good_index">
                <div class="good">
                    <div class="good-image">
                        <img :src="good.image"/>
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
                                <span class="good-reduce cubeic-remove" v-show="false" @click="handleReduce"></span>
                                <span class="good-num" v-show="false">&nbsp;&nbsp;</span>
                                <span class="good-add cubeic-add" @click="handleAdd"></span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        data: function() {
            return {
                items: [
                    {
                        "image": '//webapp.didistatic.com/static/webapp/shield/cube-ui-examples-slide01.png',
                        "goods": [
                            {
                                "id": 0,
                                "image": require('../assets/img/goods/2_P_1448945810202.jpg'),
                                "name": '哈密瓜',
                                "short": '清甜可口的哈密瓜',
                                "quantity": 5,
                                "discount": 20.55,
                                "price": 30,
                            },
                            {
                                "id": 5,
                                "image": require('../assets/img/goods/2_P_1448945810202.jpg'),
                                "name": '哈密瓜',
                                "short": '清甜可口的哈密瓜',
                                "quantity": 5,
                                "discount": 20.55,
                                "price": 30,
                            },
                            {
                                "id": 2,
                                "image": require('../assets/img/goods/2_P_1448945810202.jpg'),
                                "name": '哈密瓜',
                                "short": '清甜可口的哈密瓜',
                                "quantity": 5,
                                "discount": 20.55,
                                "price": 30,
                            },
                            {
                                "id": 3,
                                "image": require('../assets/img/goods/2_P_1448945810202.jpg'),
                                "name": '哈密瓜',
                                "short": '清甜可口的哈密瓜',
                                "quantity": 5,
                                "discount": 20.55,
                                "price": 30,
                            },
                            {
                                "id": 4,
                                "image": require('../assets/img/goods/2_P_1448945810202.jpg'),
                                "name": '哈密瓜',
                                "short": '清甜可口的哈密瓜',
                                "quantity": 5,
                                "discount": 20.55,
                                "price": 30,
                            },
                        ]
                    },
                ]
            }
        },
        methods: {
            handleAdd: function() {

            },
            handleReduce: function() {

            }
        },
        computed: {

        }
    }
</script>

<style>
    .goods {
        margin-top: 5%;
        width: 100%;
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
        width: 30%;
        text-align: right;
    }

</style>