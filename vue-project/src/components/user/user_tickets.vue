<template>
    <div id="tickets-content">
        <div class="tickets-title">
            <table>
                <tr>
                    <td>
                        Ticketname: {{ myticket['ticket_title'] }}
                    </td>
                </tr>
                <tr>
                    <td>
                        Customername: {{ myticket['customer_name'] }}
                    </td>
                    <td>
                        負責人:  {{ myticket['admin_name'] }}
                    </td> 
                </tr>
                <tr>
                    <td>
                        Time: {{ myticket['created_at'] }}
                    </td>
                </tr>
            </table>
           
        </div>
        <!-- <div class="tickets-user-dialogue">
            <table>
                <tr>
                    <th>{{ first_dialogue['created_at']}}</th>
                </tr>
                <tr>
                    <th>問題內容: {{ first_dialogue['ticket_content']}} </th>
                </tr>
                    
                 
            </table>
        </div> -->
        <div v-for="one_response in all_ticket_contents" :key="one_response">
            <div v-if="one_response['owner'] === 'customer'" class="tickets-user-dialogue">
                <table>
                    <tr>
                        <th>{{ one_response['created_at']}}</th>
                    </tr>
                    <tr>
                        <th>回覆內容: {{ one_response['ticket_content']}} </th>
                    </tr>
                    
                 
                </table>
            </div>
            <div v-else class="tickets-thomas-dialogue">
                <table>
                    <tr>
                        <th>{{ myticket['admin_name'] }}</th>
                        <th>{{ one_response['created_at']}} </th>
                    </tr>
                    <tr>
                        <th>回覆內容: </th>
                        <th> {{ one_response['ticket_content'] }}</th>
                    </tr> 
                </table>
            </div>
        </div>
        <!-- <div class="tickets-thomas-dialogue" v-if="all_ticket_contents.length > 1" >
            <table>
                <tr>
                    <th>{{ myticket['admin_name'] }}</th>
                     <th>{{ all_ticket_contents[1]['created_at']}} </th>
                </tr>
                <tr>
                    <th>回覆內容: </th>
                    <th> {{ all_ticket_contents[1]['ticket_content'] }}</th>
                </tr> 
            </table>
        </div> -->
        <div class="tickets-footer" v-if="myticket['ticket_status'] !== 'Processed'" >
            <textarea  name="message" placeholder="輸入訊息" id="message_input" cols="88" v-model="input_content"></textarea>
            <button  class="user-ticket-btn" @click="responseTicket()" ><span>傳送</span></button>
        </div>
    </div>
</template>


<script>
export default {
    inject : [
        'userdata',
        'alltickets',
        'ticketcontent'
    ],
    methods : {
        fetchTicket() {
            // https://kdmm5wrtrb.execute-api.us-west-2.amazonaws.com/dev/api/tickets/{id}
            var url = 'https://kdmm5wrtrb.execute-api.us-west-2.amazonaws.com/dev/api/tickets/'
            url += String( this.ticketcontent['ticketid'])  ;
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
                this.myticket = data['data'] ;
                console.log( "testtttttttt")
                console.log( this.myticket)
                
            })

        },
        fetch_all_contents() {
            var url = 'https://kdmm5wrtrb.execute-api.us-west-2.amazonaws.com/dev/api/tickets/contents?'
            url += 'ticket_id=' + String( this.ticketcontent['ticketid'])  ;
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
                console.log( data )
                this.all_ticket_contents = data['data'] ;
            })
        },
        responseTicket( ) {
            console.log( this.input_content)
            var url = 'https://kdmm5wrtrb.execute-api.us-west-2.amazonaws.com/dev/api/tickets/contents'
            console.log( url )
            fetch(url,{
            method: 'POST',
            headers : {
                'Content-Type': 'application/json'
            },
            body :JSON.stringify( {
                "ticket_id" : this.ticketcontent['ticketid'],
                "ticket_content" : this.input_content,
                "owner": "customer"
            })
            })
            .then( (response) => {
                if ( response.ok ) {
                    return response.json() ;
                }
            })
            .then((data) => { 
                console.log( data )
                alert( data['message'] ) ;
                this.input_content = '' ;
                this.reload() ;
            })
        },
        reload() {
            console.log('reload')
            setTimeout( this.fetch_all_contents(), 3000 ) ;
        }
    },
    data() {
        return {
            myticket : {},
            input_content : "",
            all_ticket_contents : {},
        }
    },
    created() {
        this.fetchTicket() ;
        this.fetch_all_contents() ;
    }
}
</script>

<style scoped>
    #tickets-content{
        /* background-color: gray ; */
        width: 100%;
        position: relative ;
        border-collapse:separate; 
        border-spacing:40px 10px ;
         
    }
    .tickets-title {
      
        display: flex ;
        flex-direction: row;
        position: relative ;
        width:80%;
        height: 20%;
        align-items: center ;
        margin: auto;
     
       font-weight: bolder;
       font-size: 20px;
        
    }
    .tickets-title table{
        width: 1000px;
        
    }
    textarea {
        line-height: 150%;
        height: 10vh;
        resize: none;
        width: 100%;
    }
    .tickets-user-dialogue {
        background-color: #FFEBCD;
        display: flex ;
        flex-direction: row;
        position: relative ;
        width: 80%;
        height: 15%;
        margin: auto;  
        align-items: center ;
         margin-bottom:3% ;
        
    }
    .tickets-user-dialogue td{
        align-items: right;
        color: #fff;
       
    }

     .tickets-thomas-dialogue {
        background-color: #CFECEC;
        display: flex ;
        flex-direction: row;
        position: relative ;
        width: 80%;
        height: 15%;
        margin: auto;  
        align-items: center ;
         margin-bottom:3% ;
        
    }
    .tickets-footer{
       position: relative;
       width: 80%;
       margin: auto;
       align-items: center ;
 
    }
    .user-ticket-btn{
        display: inline-block;
        border-radius: 4px;
        background-color: #fa6400;
        border: none;
        color: #FFFFFF;
        text-align: center;
        font-size: 17px;
        padding: 16px;
        width: 130px;
        transition: all 0.5s;
        cursor: pointer;
        position: relative;
        
        left: 720px;

    }
    .user-ticket-btn  span {
        cursor: pointer;
        display: inline-block;
        position: relative;
        transition: 0.5s;
        }

        .user-ticket-btn  span:after {
        content: '»';
        position: absolute;
        opacity: 0;
        top: 0;
        right: -15px;
        transition: 0.5s;
        }

        .user-ticket-btn:hover span {
        padding-right: 15px;
        }

        .user-ticket-btn:hover span:after {
        opacity: 1;
        right: 0;
        }

</style>