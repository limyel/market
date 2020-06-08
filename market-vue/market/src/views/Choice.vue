<template>
    <div id="choice">
        <div v-for="(item, item_index) in items" :key="item_index">
            <div class="goods-image">
                <img :src="item.image"/>
            </div>
            <Goods :goods="item.goods"></Goods>
        </div>
    </div>
</template>

<script>
    import Goods from "../components/Goods";

    export default {
        components: {
            Goods
        },
        computed: {
            items: function() {
                return this.$store.state.slides;
            }
        }
    }
</script>

<style>


</style>