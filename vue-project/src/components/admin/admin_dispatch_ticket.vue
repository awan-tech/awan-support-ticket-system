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
        <div class="dispatch-table-row2" v-for="data in alltickets['undo']" :key="data">
            <div class="dispatch-table-td1"> {{ data.ticket_title}} </div>
            <div class="dispatch-table-td2"> {{ data.created_at }} </div>
            <div class="dispatch-table-td3">
                <div class="engineer-select">
                    <input type="text" list="allEngineers" v-model="data.selected" v-on:input="select_undo_admin()">
                    
                    <datalist id="allEngineers"  >  
                        <option>請選擇負責人</option>
                        <option v-for="engineer in allEngineers" :key="engineer" :value="selected.admin_id"  > {{engineer.admin_name}} </option>

                    </datalist>
                </div>
            </div>
            <div  class="dispatch-table-td4"><input value="Send" type="submit" @click="dispatch_ticket(data.selected, data.ticket_id, 'Processing')" /></div>
            <div>{{data.selected}}</div> 
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
        <div class="dispatch-table-row2" v-for="data in alltickets['doing']" :key="data">
            <div class="dispatch-table-td1"> {{ data.ticket_title}} </div>
            <div class="dispatch-table-td2"> {{ data.created_at }} </div>
            <div class="dispatch-table-td3">
                <div class="engineer-select">
                    <input type="text" name="city" list="cityname">
                    <datalist id="cityname" >  
                        
                        <option>請選擇負責人</option>
                        <option v-for="engineer in allEngineers" :key="engineer" :value="engineer.admin_id" > {{engineer.admin_name}} </option>
                    </datalist>
                </div>
                 {{data.admin_name}}
            </div>
            <div  class="dispatch-table-td4"><input value="Send" type="submit" @click="dispatch_ticket(data.selected , data.ticket_id, 'Processing')" /></div>
            <div  class="dispatch-table-td4"><input value="Sucess" type="submit" @click="dispatch_ticket(data.selected, data.ticket_id, 'Processed')" /></div>
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
        <div class="dispatch-table-row2" v-for="data in alltickets['done']" :key="data">
            <div class="dispatch-table-td1"> {{ data.ticket_title}} </div>
            <div class="dispatch-table-td2"> {{ data.created_at }} </div>
            <div class="dispatch-table-td3">
                <div class="engineer-select">
                    <input type="text" name="city" list="cityname">
                    <datalist id="cityname" >  
                        
                        <option>請選擇負責人</option>
                        <option v-for="engineer in allEngineers" :key="engineer" :value="engineer.admin_id" > {{data.selected}} </option>
                    </datalist>
                   
                </div>
            </div>
            <div  class="dispatch-table-td4"><input value="Send" type="submit" @click="dispatch_ticket(data.selected , data.ticket_id, 'Processing')" /></div>
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
            temp_select_id : 0
        }
    },
    inject : [
        'userdata',
        'alltickets'
    ],
    methods : {
        dispatch_ticket( adminId, ticketId, ticket_status) {
            console.log( adminId )
            console.log( ticketId )
            console.log( ticket_status )
            var url = 'https://kdmm5wrtrb.execute-api.us-west-2.amazonaws.com/dev/api/tickets/assign'
            console.log( url )
            fetch(url,{
            method: 'POST',
            headers : {
                'Content-Type': 'application/json'
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
                console.log( data )
                alert( data['data']['message'])
            })
        },
        async find_engineer() {
            var url = 'https://kdmm5wrtrb.execute-api.us-west-2.amazonaws.com/dev/api/users?role=Engineer'
            console.log( url )
            await fetch(url,{
            method: 'GET',
            headers : {
                'Content-Type': 'application/json'
            }
            })
            .then( (response) => {
                if ( response.ok ) {
                    return response.json() ;
                }
            })
            .then((data) => { 
                console.log( data['data'] ) ;
                this.allEngineers = this.allEngineers.concat( data['data'] )
            })

            await this.find_engineer_supervisor() ;
        },
        find_engineer_supervisor() {
            var url = 'https://kdmm5wrtrb.execute-api.us-west-2.amazonaws.com/dev/api/users?role=Engineer Supervisor'
            
            console.log( url )
            fetch(url,{
            method: 'GET',
            headers : {
                'Content-Type': 'application/json'
            }
            })
            .then( (response) => {
                if ( response.ok ) {
                    return response.json() ;
                }
            })
            .then((data) => { 
                console.log( data['data'] ) ;
                this.allEngineers = this.allEngineers.concat( data['data'] )
            })
        },
        select_undo_admin( index) {
            this.temp_select_id = this.allEngineers['undo'][index]['admin_id'] ;
            // this.allEngineers['undo'][index]
            console.log( this.temp_select_id )
        },
        get_all_tickets() {
            // let url = 'https://kdmm5wrtrb.execute-api.us-west-2.amazonaws.com/dev/api/tickets'
            // for( let i ; i < this.allEngineers.length ; i ++ ) {
            //     let temp = url + allEngineers[i] ;
            // } // for
        }
    },
    mounted() {
        this.find_engineer() ;
        this.find_engineer_supervisor() ;
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