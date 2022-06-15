<template>
    <div class="dispatch-table">
        <div>
           未配單
        </div>
        <div class="dispatch-table-row1">
            <div class="dispatch-table-th1">ticket title</div>
            <div class="dispatch-table-th2">deadline</div>
            <div class="dispatch-table-th3">負責人</div>
            <div class="dispatch-table-th4"></div>
        </div>
        <div class="dispatch-table-row2" v-for="(data, index) in every_tickets['not_proccess']" :key="data">
            <div class="dispatch-table-td1"> {{ data.ticket_title}} </div>
            <div class="dispatch-table-td2"> {{ data.created_at }} </div>
            <div class="dispatch-table-td3">
                <div class="engineer-select">
                    <input type="text" name="city" list="cityname" v-model="data.selected" v-on:input="get_engineer_id(index, data.selected, 'not_proccess')">
                    <datalist id="cityname"> 
                        <option value="">請選擇負責人</option> 
                        <option v-for="engineer in allEngineers" :key="engineer" :value="engineer.admin_name" > {{engineer.admin_name}} </option>
                    </datalist>
                </div>
            </div>
            <div  class="dispatch-table-td4"><input value="Send" type="submit" @click="dispatch_ticket(data.selected_id, data.ticket_id, 'Processing')" /></div>
            
            
        </div>
      
        <div>
            已配單
        </div>

        <div class="dispatch-table-row1">
            <div class="dispatch-table-th1">ticket title</div>
            <div class="dispatch-table-th2">deadline</div>
            <div class="dispatch-table-th3">負責人</div>
            <div class="dispatch-table-th4"></div>
            <div class="dispatch-table-th4"></div>
        </div>
        <div class="dispatch-table-row2" v-for="(data, index) in every_tickets['proccessing']" :key="data">
            <div class="dispatch-table-td1"> {{ data.ticket_title}} </div>
            <div class="dispatch-table-td2"> {{ data.created_at }} </div>
            <div class="dispatch-table-td3">
                <div class="engineer-select">
                    現在負責人: {{data.admin_name}}
                    <input type="text" name="city" list="cityname" v-model="data.selected" v-on:input="get_engineer_id(index, data.selected, 'proccessing')">
                    <datalist id="cityname"> 
                        <option value="">請選擇負責人</option> 
                        <option v-for="engineer in allEngineers" :key="engineer" :value="engineer.admin_name" > {{engineer.admin_name}} </option>
                    </datalist>
                </div>
                 
            </div>
            <div  class="dispatch-table-td4"><input value="Send" type="submit" @click="dispatch_ticket(data.selected_id , data.ticket_id, 'Processing')" /></div>
            <div  class="dispatch-table-td4"><input value="Sucess" type="submit" @click="dispatch_ticket(data.selected_id, data.ticket_id, 'Processed')" /></div>
        </div>
        <div>
           已完成
        </div>
        <div class="dispatch-table-row1">
            <div class="dispatch-table-th1">ticket title</div>
            <div class="dispatch-table-th2">deadline</div>
            <div class="dispatch-table-th3">負責人</div>
            <div class="dispatch-table-th4"></div>          
        </div>
        <div class="dispatch-table-row2" v-for="(data, index) in every_tickets['proccessed']" :key="data">
            <div class="dispatch-table-td1"> {{ data.ticket_title}} </div>
            <div class="dispatch-table-td2"> {{ data.created_at }} </div>
            <div class="dispatch-table-td3">
                <div class="engineer-select">
                    現在負責人: {{data.admin_name}}
                    <input type="text" name="city" list="cityname" v-model="data.selected" v-on:input="get_engineer_id(index, data.selected, 'proccessed')">
                    <datalist id="cityname"> 
                        <option value="">請選擇負責人</option> 
                        <option v-for="engineer in allEngineers" :key="engineer" :value="engineer.admin_name" > {{engineer.admin_name}} </option>
                    </datalist>
                </div>
            </div>
            <div  class="dispatch-table-td4"><input value="Send" type="submit" @click="dispatch_ticket(data.selected_id , data.ticket_id, 'Processing')" /></div>
        </div>
    </div>
    
</template>

 <script>
 export default {
    data() {
        return {
            oneTicket : {},
            allEngineers : [],
            selected : '',
            temp_select_id : 0,
            every_tickets : {
                not_proccess : [],
                proccessing : [],
                proccessed : []
            },
            tickets_page : '0'
        }
    },
    inject : [
        'alltickets',
        'jwtToken'
    ],
    methods : {
        dispatch_ticket( adminId, ticketId, ticket_status) {
            if ( adminId === undefined || ticketId === '' || ticket_status === '' ) {
                alert( '請選擇負責人')
                return false ;
            }
                
            // console.log( adminId )
            // console.log( ticketId )
            // console.log( ticket_status )
            var url = 'https://u7j2emffl8.execute-api.us-west-2.amazonaws.com/dev/api/tickets/assign'
            // console.log( url )
            fetch(url,{
            method: 'POST',
            headers : {
                'Content-Type': 'application/json',
                'Authorization' : this.jwtToken.jwt
            },
            body : JSON.stringify({
                'admin_id' : adminId,
                'ticket_id' : ticketId,
                'ticket_status' : ticket_status
            })
            })
            .then( (response) => {
                if ( response.ok ) {
                    return response.json() ;
                }
            })
            .then((data) => { 
                // console.log( data )
                alert( data['data']['message'])
                this.reload() ;
            })
        },
        async find_engineer() {
            var url = 'https://u7j2emffl8.execute-api.us-west-2.amazonaws.com/dev/api/users?role=Engineer'
            console.log( url )
            await fetch(url,{
            method: 'GET',
            headers : {
                'Content-Type': 'application/json',
                'Authorization' : this.jwtToken.jwt
            }
            })
            .then( (response) => {
                if ( response.ok ) {
                    return response.json() ;
                }
            })
            .then((data) => { 
                // console.log( data['data'] ) ;
                this.allEngineers = this.allEngineers.concat( data['data'] )
            })

            await this.find_engineer_supervisor() ;
        },
        find_engineer_supervisor() {
            var url = 'https://u7j2emffl8.execute-api.us-west-2.amazonaws.com/dev/api/users?role=Engineer Supervisor'
            
            // console.log( url )
            fetch(url,{
            method: 'GET',
            headers : {
                'Content-Type': 'application/json',
                'Authorization' : this.jwtToken.jwt
            }
            })
            .then( (response) => {
                if ( response.ok ) {
                    return response.json() ;
                }
            })
            .then((data) => { 
                // console.log( data['data'] ) ;
                this.allEngineers = this.allEngineers.concat( data['data'] )
            })
        },
        get_engineer_id( index ,name, status) {
            for ( let i of this.allEngineers) {
               if ( i.admin_name === name ) {
                    this.every_tickets[status][index].selected_id = i.admin_id ;
                    // console.log( this.every_tickets[status][index].selected_id )
               }
           }
        },
        getAlltickets() {
            let address = 'https://u7j2emffl8.execute-api.us-west-2.amazonaws.com/dev/api/tickets?page=' + this.tickets_page + '&status=all&user_id=0&role=0' ;

            fetch( address ,{
            method: 'GET',
            headers : {
                'Content-Type': 'application/json',
                'Authorization' : this.jwtToken.jwt
            },
            })
            .then( (response) => {
                if ( response.ok ) {
                    return response.json() ;
                }
            })
            .then((data) => { 
                // console.log ('all')
                // console.log( data ) ;
                for( let i of data['data'] ) {
                    if ( i['ticket_status'] === 'Not Processed') {
                        this.every_tickets['not_proccess'].push( i ) ;
                    }
                    else if ( i['ticket_status'] === 'Processing' ) {
                        this.every_tickets['proccessing'].push( i ) ;
                    }
                    else if ( i['ticket_status'] === 'Processed' ) {
                        this.every_tickets['proccessed'].push( i ) ;
                    }
                }
                // console.log( this.every_tickets )
            })
        },
        reload() {
            this.every_tickets = {
                not_proccess : [],
                proccessing : [],
                proccessed : []
            }
            setTimeout( this.getAlltickets(), 3000 ) ;
        }
    },
    created() {
        this.find_engineer() ;
        this.find_engineer_supervisor() ;
        this.getAlltickets()
    },
 }
 </script>


<style scoped>
.dispatch-table{
    display: table;
    position: relative;   
    width: 80%;
    height: 10%;
    left: 10%;
    top: 5%;
     /* padding-left: 10px;
     padding-right: 10px; */
    table-layout: fixed;
    
}
.dispatch-table .dispatch-table-row1{
    display: table-row; 
    height: 10%;
}
.dispatch-table .dispatch-table-th1{
   display: table-cell;
   /* font-weight: bold; */
   /* height: 0px; */
   width: 30%;
   border: 1px solid gray;
   text-align: center;
   vertical-align: middle;
   background-color:#E5E5E5;
   
}
.dispatch-table .dispatch-table-th2{
   display: table-cell;
   /* font-weight: bold; */
   /* height: 30px; */
   width: 15% ;
   border: 1px solid gray;
   text-align: center;
   vertical-align: middle;
   background-color:#E5E5E5;
}
.dispatch-table .dispatch-table-th3{
   display: table-cell;
   /* font-weight: bold; */
   /* height: 10px; */
   width: 20%;
   border: 1px solid gray;
   text-align: center;
   vertical-align: middle;
   background-color:#E5E5E5;
}
.dispatch-table .dispatch-table-th4{
   display: table-cell;
   /* font-weight: bold; */
   /* height: 10px; */
   width: 7%;
    border: 1px solid gray;
   text-align: center;
   vertical-align: middle;
   background-color:#E5E5E5;

}
.dispatch-table .dispatch-table-row2{
     display: table-row; 
    
     table-layout: fixed;
     height: 10%;
     
     /* box-shadow: 0px 0px 9px 0px rgba(0, 0, 0, 0.1); */
}
.dispatch-table .dispatch-table-td1{
     display: table-cell;
     /* height: 10px; */
     /* width: 20%; */
     border: 1px solid gray; 
     text-align: center;
     vertical-align: middle;
     table-layout:fixed;
     overflow: hidden;
     text-overflow: ellipsis;
      white-space: nowrap;
      background-color: #fff;
     

}
.dispatch-table .dispatch-table-td2{
    display: table-cell;
     /* height: 10px; */
     /* width: 10px; */
     border: 1px solid gray; 
     text-align: center;
     vertical-align: middle;
     overflow: hidden;
     text-overflow: ellipsis;
      background-color: #fff;
}
.dispatch-table .dispatch-table-td3{
    display: table-cell;
     /* height: 10px; */
      /* width: 125px; */
     border: 1px solid gray; 
     text-align: center;
     vertical-align: middle;
     overflow: hidden;
     text-overflow: ellipsis;
      background-color: #fff;
}
.dispatch-table .dispatch-table-td4{
    display: table-cell;
     /* height: 10px; */
    width: 10px;
     border: 1px solid gray; 
     text-align: center;
     vertical-align: middle;
      background-color: #fff;

}
.engineer-select select {
  background: #919497;
  color: #fafafa;
  /* margin: 15px; */
  width: 100%;
  height: 100%;
  padding: 8px;
  position: relative;
  appearance: none;
}
 
option {
  appearance: none;
  background: rgb(106, 101, 101);
  position: absolute;
}


input[type=submit]{
 
  height: 50%;
  font-size: 0.5em;
  font-weight: bold;
  font-family: "Open Sans";
  text-transform: uppercase;
  color: #696666;
  border-radius: 1em;
  border: 0.15em solid #6d6b66;
}
input[type="submit"]:hover {
    color: #fff;
    background-color: #6d6b66;
    border-color: #6d6b66;
    -webkit-transition: all 0.3s ease;
}



</style>