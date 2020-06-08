<template>
    <div id="category">
        <div class="search">
            <span>搜索<i class="cubeic-search"></i></span>
        </div>
        <cube-scroll class="leftpanels">
            <ul>
                <li v-for="(category, index) in categories" @click='selectCategory(category.id)' :class="isActive === category.id? 'active': ''" :key='index'>
                    {{category.name}}
                </li>
            </ul>
        </cube-scroll>
        <cube-scroll class="rightpanels">
            <Goods :goods="activeCategory.goods"></Goods>
        </cube-scroll>
    </div>
</template>

<script>
    import Goods from "../components/Goods";

    export default {
        components: {
            Goods
        },
        data: function() {
            return {
                activeId: 0,
                category: {}
            }
        },
        methods: {
            selectCategory: function(id) {
                this.activeId = id;
                this.axios.get('/api/goods/categories/' + this.activeId + '/').then(res => {
                    this.category = res.data;
                    this.activeId = this.activeId === 0? this.category.id: this.activeId;
                });
            }
        },
        computed: {
            categories: function() {
                let categories = this.$store.state.categories? this.$store.state.categories: [];
                return categories;
            },
            isActive: function() {
                let id = this.activeId === 0? this.$store.state.categories[0].id: this.activeId;
                return id;
            },
            activeCategory: function() {
                return this.category;
            }
        },
        mounted() {
            let id = this.$route.query.id? this.$route.query.id: 0;
            console.log(id);
            // this.axios.get('/api/goods/categories/' + this.activeId + '/').then(res => {
            //     this.category = res.data;
            //     this.activeId = this.activeId === 0? this.category.id: this.activeId;
            // });
            this.selectCategory(id);
        }
    }
</script>

<style lang="stylus" scoped>
    .active
        background-color white
        color gray

    #category
        display flex
        margin-top 15%

    .leftpanels
        width 20%
        font-size 1.2em
        text-align center
        border-right 1px solid lightgray
        background-color lightgray
        height 620px
        li
            height 50px
            line-height 50px

    .rightpanels
        width 80%
        height 620px
        overflow scroll

    .search
        position fixed
        top 0
        width 100%
        padding-left 10%
        border-bottom 1px solid lightgray
        z-index 1000
        span
            display inline-block
            width 80%
            text-align center
            padding 2% 0
            background-color lightgray
            font-size 1.2em;



</style>