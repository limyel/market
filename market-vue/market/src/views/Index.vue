<template>
    <div id="index">
        <SearchBar></SearchBar>
        <cube-slide ref="slide" :data="slides" @change="changePage">
            <cube-slide-item v-for="(item, index) in slides" :key="index" @click.native="clickHandler(item, index)">
                <a href="#">
                    <img :src="item.image">
                </a>
            </cube-slide-item>
        </cube-slide>
        <div class="categories">
            <div v-for="(category, index) in categories" :key="index" class="category">
                <router-link :to="{name: 'Category', query: {id: category.id}}"><img :src="category.image"/></router-link>
                <p>{{category.name}}</p>
            </div>
        </div>

        <cube-scroll-nav-bar :current="current" :labels="labels" @change="changeHandler" />
        <router-view></router-view>
    </div>
</template>

<script>
    import SearchBar from "../components/SearchBar";

    export default {
        data: function() {
            return {
                current: '精选',
                labels: [
                    '精选',
                    '限时抢购',
                    '疯狂折扣',
                    '新品推荐'
                ],
            }
        },
        components: {
            SearchBar,
        },
        methods: {
            changePage(current) {
                // console.log('当前轮播图序号为:' + current)
            },
            clickHandler(item, index) {
                console.log(item, index)
            },
            changeHandler: function(cur) {
                console.log(cur);
                switch(cur) {
                    case '精选': this.$router.push('/index/choice');break;
                    case '限时抢购': this.$router.push('/index/rush');break;
                    case '疯狂折扣': this.$router.push('/index/discount');break;
                    case '新品推荐': this.$router.push('/index/new');
                }
            }
        },
        computed: {
            slides: function() {
                let slides = this.$store.state.slides? this.$store.state.slides: {};
                return slides;
            },
            categories: function() {
                let categories = this.$store.state.categories? this.$store.state.categories: {};
                return categories;
            }
        },
        beforeCreate() {
            this.axios.get('/api/goods/slides/').then(res => {
                this.$store.commit('setSlides', res.data);
            });
            this.axios.get('/api/goods/categories/').then(res => {
                this.$store.commit('setCategories', res.data);
            });

        }
    }
</script>

<style>

    .categories {
        display: flex;
        flex-wrap: wrap;
        margin-top: 3%;
    }

    .category {
        width: 20%;
        margin-top: 2%;
    }
    .category img {
        width: 80%;
        height: 80%;
        margin-left: 10%;
    }
    .category p {
        font-size: 0.8em;
        text-align: center;
    }

    .cube-scroll-nav-bar {
        margin-top: 5%;
    }

    .cube-slide-item img {
        width: 100%;
        object-fit: cover;
    }
</style>