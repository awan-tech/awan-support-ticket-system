<template>
    <div class="thomas-all">
        <div id="deadline-table" class="thomas-right" >
            <li class="deadline-header">
                <div class="deadline-tr">問題標題</div>
                <div class="deadline -tr">Created At</div>
            </li>
            <li class="deadline-row" v-for="temp in alltickets['done']" :key="temp" @click="viewTicket(temp['ticket_id'], temp['ticket_title'], temp['admin_id'])">
                <div class="deadline-td1">{{ temp['ticket_title']}} </div>
                <div class="deadline-td2">{{ temp['created_at']}}</div>
            </li>

        </div>

    </div>
</template>

<script>
export default {
    emits:[
        'all_ticket_contents'
    ],
    data() {
        return {
            oneTicket : {}
        }
    },
    inject : [
        'userdata',
        'alltickets'
    ],
    methods: {
        viewTicket( ticketid, tickettitle, ticket_admin_name ) {
            this.$emit('all_ticket_contents', ticketid, tickettitle, ticket_admin_name )
            this.$router.push('/userhome/tickets')
        }
    },
}
</script>

<style scoped>

#pending-btn {
    border: 0;
    display: flex;
    flex-direction: column;
    width: 100%;
    max-width: 140px;
    height: 50px;
    /* border-radius: 0em; */
    overflow: hidden;
    position: relative;
    top: 50px;
    left: 40px;
   }
   
   #pending-btn div {
    transform: translateY(0px);
    width: 100%;
   }
   
   #pending-btn,
   #pending-btn div {
    transition: 0.6s cubic-bezier(.16,1,.3,1);
   }
   
   #pending-btn div span {
    display: flex;
    align-items: center;
    justify-content: space-between;
    height: 50px;
    padding: 0.75em 1.125em;
   }
   
   #pending-btn div:nth-child(1) {
    background-color: #1e90ff;
   }
   
   #pending-btn div:nth-child(2) {
    background-color: #dc7221;
   }
   
   #pending-btn:hover {
    box-shadow: 0 0.625em 1em 0 rgba(220, 148, 33, 0.35);
   }
   
   #pending-btn:hover div {
    transform: translateY(-50px);
   }
   
   #pending-btn p {
    font-size: 17px;
    font-weight: bold;
    color: #ffffff;
    
   }
   
   #pending-btn:active {
    transform: scale(0.95);
   }
   



.thomas-all{
    position: relative ;
    display: flex ;
    width: 100%;
}

.thomas-left {
    position: relative ;
    display: flex ;
    flex-direction: column ;
    width: 20%;
}
.thomas-right {
    background-color: rgb(255, 255, 255);
    position: relative ;
    display: flex ;
    flex-direction: column ;
    margin: auto;
    width: 70%;
    height: 100%;
}

   
#deadline-table {
    /* display:table; */
    position: relative;
    top: 5%;
    border-collapse: collapse;
    font-weight: bold;
    table-layout: fixed;
    
  }
   #deadline-table li{
        border-radius: 3px;
        padding: 25px 30px;
        display: flex;
        justify-content: space-between;
   }
  #deadline-table .deadline-header{
       background-color: #e5e5e5;
     font-size: 20px;
     font-weight: bolder;
     text-transform: uppercase;
     letter-spacing: 0.03em;

  }
  #deadline-table .deadline-row {
   
    background-color: rgb(255, 255, 255);
     box-shadow: 0px 0px 9px 0px rgba(0, 0, 0, 0.1);
  }
   #deadline-table .deadline-row:hover {
    background-color: #797979;
         color: rgb(255, 255, 255);
  }
  #deadline-table .deadline-td1 {

         flex-basis: 70%;
         overflow: hidden;
         text-overflow: ellipsis;
    }
    #deadline-table .deadline-td12 {
        flex-basis: 30%;
    }
  

  .onoffswitch {
    position: relative; width: 93px;
    /* -webkit-user-select:none; -moz-user-select:none; -ms-user-select: none; */
}
.onoffswitch-checkbox {
    position: absolute;
    opacity: 0;
    pointer-events: none;
}
.onoffswitch-label {
    display: block; overflow: hidden; cursor: pointer;
    border: 2px solid #999999; border-radius: 0px;
}
.onoffswitch-inner {
    display: block; width: 200%; margin-left: -100%;
    transition: margin 0.3s ease-in 0s;
}
.onoffswitch-inner:before, .onoffswitch-inner:after {
    display: block; float: left; width: 50%; height: 25px; padding: 0; line-height: 25px;
    font-size: 14px; color: white; font-family: Trebuchet, Arial, sans-serif; font-weight: bold;
    box-sizing: border-box;
}
.onoffswitch-inner:before {
    content: "Deadline";
    padding-left: 5px;
    background-color: #34A7C1; color: #FFFFFF;
    text-align: left;
}
.onoffswitch-inner:after {
    content: "New";
    padding-right: 5px;
    background-color: #949494; color: #FFFFFF;
    text-align: right;
}
.onoffswitch-switch {
    display: block; width: 16px; margin: 4.5px;
    background: #FFFFFF;
    position: absolute; top: 0; bottom: 0;
    right: 64px;
    border: 2px solid #999999; border-radius: 18px;
    transition: all 0.3s ease-in 0s; 
}
.onoffswitch-checkbox:checked + .onoffswitch-label .onoffswitch-inner {
    margin-left: 0;
}
.onoffswitch-checkbox:checked + .onoffswitch-label .onoffswitch-switch {
    right: 0px; 
}
</style>