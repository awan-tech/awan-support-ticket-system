<template>
    <div>
        <div>
            <button>
               更改Engineer 資料 
            </button>
        </div>
        <div>
            <button @click="change_to_dispatch">
                分派tickets
            </button>
        </div>
        <div>
            <button @click="change_to_create">
                新增Engineer帳號
            </button>
        </div>
    </div>
</template>

<script>
export default {
    
    methods: {
        change_to_create() {
            this.$router.push('/home/admin_create_engineer') ;
        },
        change_to_dispatch() {
            this.$router.push('/home/admin_dispatch_ticket') ;
        }
    },

}
</script>

<style scoped>

</style>