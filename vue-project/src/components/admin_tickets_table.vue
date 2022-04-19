<template>
    <div class="tickets-table">
        <div class="tickets-table-left">
            已處理
        </div>
        <div class="tickets-table-right">
            正在處理
        </div>
    </div>
</template>

<script>
export default {
    
}
</script>

<style scoped>
    .tickets-table {
        width: 100%;
        position: relative ;
        display: flex ;
        
    }
    .tickets-table-left {
        /* background-color: rgb(105, 4, 4); */
        position: relative ;
        display: flex ;
        flex-direction: column ;
        width: 20%;
        align-items: center;
    }
    .tickets-table-right {
        /* background-color: aquamarine; */
        position: relative ;
        display: flex ;
        flex-direction: column ;
        width: 80%;
        align-items: center;
    }
</style>
