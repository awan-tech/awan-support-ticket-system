<template>
    <div class="tickets-table">
         
        <div class="tickets-table-left">
            <li class="table-header">
                    <div class="tickets-table-left-tr">待處理</div>
            </li>
            <li class="table-row" v-for="data in doing" :key="data">
                     <div class="user-table-td1" data-label="Job Id">{{ data.ticket_title}} </div>
            </li>
            <!-- <li class="table-row">
                     <div class="user-table-td1" data-label="Job Id">4223543556456435214246532438787548789385498689589328dbs796987ddddddddd</div>
            </li>
            <li class="table-row">
                     <div class="user-table-td1" data-label="Job Id">4223543556456435214246532438787548789385498689589328dbs796987ddddddddd</div>
            </li>
            <li class="table-row">
                     <div class="user-table-td1" data-label="Job Id">4223543556456435214246532438787548789385498689589328dbs796987ddddddddd</div>
            </li>
            <li class="table-row">
                     <div class="user-table-td1" data-label="Job Id">4223543556456435214246532438787548789385498689589328dbs796987ddddddddd</div>
            </li>
            <li class="table-row">
                     <div class="user-table-td1" data-label="Job Id">4223543556456435214246532438787548789385498689589328dbs796987ddddddddd</div>
            </li> -->

        </div>
        <div class="tickets-table-right">
            <li class="table-header">
                    <div class="tickets-table-right-tr">已處理</div>
            </li>
            <li class="table-row" v-for="data in undo" :key="data">
                     <div class="user-table-td1" data-label="Job Id">{{ data.ticket_title}} </div>
            </li>
            <!-- <li class="table-row">
                     <div class="user-table-td1" data-label="Job Id">4223543556456435214246532438787548789385498689589328dbs796987ddddddddd</div>
            </li>
            <li class="table-row">
                     <div class="user-table-td1" data-label="Job Id">4223543556456435214246532438787548789385498689589328dbs796987ddddddddd</div>
            </li> -->

            
        </div>
    </div>
</template>

<script>
export default {
    inject : [
        'userdata'
    ],
    data() {
        return {
            doing : [],
            done : [],
        }
    },
    methods: {
        classify() {
            this.doing = this.userdata['tickets'].filter( temp => temp.ticket_status == 'doing');
            this.done = this.userdata['tickets'].filter( temp => temp.ticket_status == 'undo');
            console.log( ' what is doing ')
            console.log( this.doing )
        }
    },
    mounted() {
        this.classify() ;
    },
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
       position: relative;   
        width: 350px;
        left: 50px;
        top: 30px;
     /* padding-left: 10px;
     padding-right: 10px; */
        table-layout: fixed;
    
    }
    .tickets-table-left li{
        border-radius: 3px;
        padding: 25px 30px;
        display: flex;
        justify-content: space-between;
    }
    .tickets-table-left .table-header {
     background-color: #e5e5e5;
     font-size: 20px;
     font-weight: bolder;
     text-transform: uppercase;
     letter-spacing: 0.03em;
    }
    .tickets-table-left .table-row {
     background-color: #fff;
     box-shadow: 0px 0px 9px 0px rgba(0, 0, 0, 0.1);
    }
    .tickets-table-left .table-row:hover {
         background-color: rgb(153, 164, 112);
         color: rgb(255, 253, 253);
    }
    .tickets-table-left .user-table-td1 {
         flex-basis: 80%;
         overflow: hidden;
         text-overflow: ellipsis;
    }

    .tickets-table-right {
       position: relative;   
        width: 350px;
        left: 150px;
        top: 30px;
     /* padding-left: 10px;
     padding-right: 10px; */
        table-layout: fixed;
    }
    .tickets-table-right li{
        border-radius: 3px;
        padding: 25px 30px;
        display: flex;
        justify-content: space-between;
    }
    .tickets-table-right .table-header {
     background-color: #e5e5e5;
     font-size: 20px;
     font-weight: bolder;
     text-transform: uppercase;
     letter-spacing: 0.03em;
    }
    .tickets-table-right .table-row {
     background-color: #fff;
     box-shadow: 0px 0px 9px 0px rgba(0, 0, 0, 0.1);
    }
    .tickets-table-right .table-row:hover {
         background-color: rgb(153, 164, 112);
         color: rgb(255, 253, 253);
    }
    .tickets-table-right .user-table-td1 {
         flex-basis: 80%;
         overflow: hidden;
         text-overflow: ellipsis;
    }
</style>
