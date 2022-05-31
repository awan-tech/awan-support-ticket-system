<template>
    <div class="tickets-table">
       
        <div class="tickets-table-left">
            <li class="table-header">
                    <div class="tickets-table-left-tr">尚未處理</div>
            </li>
            <li class="table-row" v-for="data in alltickets['undo']" :key="data" @click="viewTicket(data['ticket_id'], data['ticket_title'], data['admin_id'])">
                     <div class="user-table-td1" data-label="Job Id">{{ data.ticket_title}} </div>
            </li>
         
        </div>
        <div class="tickets-table-right">
            <li class="table-header">
                    <div class="tickets-table-right-tr">待處理</div>
            </li>
            <li class="table-row" v-for="data in alltickets['doing']" :key="data" @click="viewTicket(data['ticket_id'], data['ticket_title'], data['admin_id'])">
                     <div class="user-table-td1" data-label="Job Id">{{ data.ticket_title}} </div>
            </li>

            
        </div>
    </div>
</template>

<script>
export default {
    inject : [
        'userdata',
        'alltickets',
    ],
    data() {
        return {
            doing : [],
            undo : []
        }
    },
    methods: {
        viewTicket( ticketid, tickettitle, ticket_admin_name ) {
      
            this.$emit('all_ticket_contents', ticketid, tickettitle, ticket_admin_name ) ; // back to template
            this.$router.push('/userhome/tickets')
        }
    },
    mounted() {
        // this.classify() ;
    },
}
</script>

<style scoped>
    .tickets-table {
        width: 100%;
        position: relative ;
        display: flex ;
        flex-direction: row ;
    }
    .tickets-table-left {
        position: relative;   
        width: 40%;
        left: 50px;
        top: 30px;
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
         background-color: #797979;
         color: rgb(255, 253, 253);
    }
    .tickets-table-left .user-table-td1 {
         flex-basis: 80%;
         overflow: hidden;
         text-overflow: ellipsis;
    }

    .tickets-table-right {
       position: relative;   
        width: 40%;
        left: 150px;
        top: 30px;
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
         background-color: #797979;
         color: rgb(255, 253, 253);
    }
    .tickets-table-right .user-table-td1 {
         flex-basis: 80%;
         overflow: hidden;
         text-overflow: ellipsis;
    }
</style>
