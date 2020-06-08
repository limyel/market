<template>
    <div id="address">
        <Header :title="'我的地址'"></Header>
        <input placeholder="收货人姓名" v-model="name" type="text"/>
        <input placeholder="手机号" v-model="phone" type="text"/>
        <input placeholder="收货地址" v-model="address" type="text"/>
        <cube-button @click="handleAdd">添加收货地址</cube-button>
        <br/>
        <br/>
        <hr/>
        <div class="address" v-for="(addr, index) in getaddresses" :key="index">
            <div class="info">
                {{addr.name}}
                <br/>
                {{addr.phone}}
                <br/>
                {{addr.address}}
            </div>
            <p class="button" @click="del(index)">
                删除
            </p>
        </div>
    </div>
</template>

<script>
    import Header from "../components/Header";

    export default {
        data() {
            return {
                name: '',
                phone: '',
                address: '',
                addresses: []
            }
        },
        components: {
            Header,
        },
        methods: {
            handleAdd: function() {
                this.axios.post('/api/user_operations/address/', {name: this.name, phone: this.phone, address: this.address}).then(res => {
                    this.addresses.push(res.data);
                    this.name = '';
                    this.phone = '';
                    this.address = '';
                })
            },
            del(index) {
                let id = this.addresses[index].id;
                this.axios.delete('/api/user_operations/address/' + id + '/').then(res => {
                    this.axios.get('/api/user_operations/address/').then(res => {
                        this.addresses = [];
                        this.addresses = res.data;
                    })
                });

            }
        },
        created() {
            this.axios.get('/api/user_operations/address/').then(res => {
                this.addresses = res.data;
            })
        },
        computed: {
            getaddresses() {
                return this.addresses;
            }
        }
    }
</script>

<style lang="stylus" scoped>
    #address
        padding-top 15%
        input
            width 80%
            margin-left 10%
            line-height 30px
            margin-bottom 5%


    .address
        font-size 1.2em
        padding-left 10%
        margin 5% 0
        line-height 150%
        display flex
        .info
            width 80%
        .button
            width 20%
            background-color gray
            text-align center
</style>