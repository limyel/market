<template>
    <div id="good">
        <Header :title="good.name"></Header>
        <div class="content">
            <img class="good-image" :src="good.images[0].image"/>
            <div class="good-info">
                <div class="good-price">
                    <span class="discount">{{good.discount}}</span>
                    &nbsp;&nbsp;&nbsp;
                    <span class="price">{{good.price}}</span>
                </div>
                <div class="good-describe">
                    <p class="good-name">{{good.name}}</p>
                    <p class="good-short">{{good.short}}</p>
                </div>
                <div class="good-weight">
                    <span class="cubeic-alert"></span>{{good.weight}}&nbsp;&nbsp;
                    <span class="cubeic-location"></span>{{good.production}}&nbsp;&nbsp;
                </div>
            </div>
            <br/>
            <hr width="80%"/>
            <br/>
            <div class="detail">
                <img :src="good.detail"/>
            </div>
        </div>
        <div id="cartbar">
            <p class="favorite" @click="handleFavorite"><span :class="isFavorite === true? 'cubeic-like is-favorite': 'cubeic-like'"></span></p>
            <p class="cart"><span class="cubeic-mall"></span></p>
            <p class="reduce"><span @click="handleReduce(good.id)" class="cubeic-remove"></span></p>
            <p class="num" :id="good.id">0</p>
            <p class="add"><span @click="handleAdd(good.id)" class="cubeic-add"></span></p>
        </div>
    </div>
</template>

<script>
    import Header from "../components/Header";

    export default {
        components: {
            Header,
        },
        data: function() {
            return {
                good: {},
                favorite: false
            }
        },
        methods: {
            handleFavorite: function() {
                if(this.favorite) {
                    this.axios.delete("/api/user_operations/" + this.good.id + '/').then(res => {
                        this.favorite = false;
                    })
                } else {
                    this.axios.post("/api/user_operations/", {"good": this.good.id}).then(res => {
                        this.favorite = true;
                    })
                }

            },
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
            isFavorite() {
                return this.favorite;
            }
        },
        created() {
            let id = this.$route.params.id;
            this.axios.get('/api/goods/' + id + '/').then(res => {
                this.good = res.data;
                this.axios.get('/api/user_operations/' + this.good.id + '/').then(res => {
                    console.log(res.data);
                    if(res.data.code === 0)
                        this.favorite = true;
                    else
                        this.favorite = false;
                });
            });
            this.$emit("isDisplay");
        },
        destroyed() {
            this.$emit("isDisplay");
        }
    }
</script>

<style lang="stylus" scoped>
    #cartbar
        background-color white
        position fixed
        z-index 1200
        bottom 0
        left 0
        height 70px
        line-height 70px
        display flex
        width 100%
        font-size 2em
        color darkgrey
        text-align center
        .favorite
            width 20%
            color darkgrey
        .cart
            width 20%
        .reduce
            width 20%
        .num
            width 20%
        .add
            width 20%

    #good
        margin-top 15%
        .content
            width 100%
            .good-image
                padding 0 10%
                width 80%
                height 50%
            .good-info
                padding 5% 5%
                .good-price
                    .discount
                        font-size 1.5em
                        color orangered
                    .price
                        font-size 1.1em
                        text-decoration line-through
                        color gray
                .good-describe
                    margin-top 5%
                    .good-name
                        font-size 1.5em
                        font-weight bold
                        margin-bottom 3%
                    .good-short
                        font-size 1.1em
                .good-weight
                    margin-top 5%
                    font-size 0.8em
                    color gray
            .detail
                img
                    width 100%;

    .is-favorite
        color red
</style>