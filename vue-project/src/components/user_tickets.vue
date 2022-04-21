<template>
    <div id="tickets-content">
        <div class="tickets-title">
            <table>
                <tr>
                    <td>
                        ticketname: {{ ticketcontent['title'] }}
                    </td>
                </tr>
                <tr>
                    <td>
                        customrname: {{ userdata['username'] }}
                    </td>
                    <td>
                        負責人:
                    </td>
                </tr>
                <tr>
                    <td>
                        time:
                    </td>
                </tr>
            </table>
           
        </div>
        <div class="tickets-user-dialogue">
            <table>
                <tr>
                    <th>yy/ds</th>
                </tr>
                <tr>
                    <th>問題內容:</th>
                </tr>
                    
                 
            </table>
        </div>
        <div class="tickets-thomas-dialogue">
            <table>
                <tr>
                    <th>(工程師名字)</th>
                     <th>yy/ds</th>
                </tr>
                <tr>
                    <th>回覆內容:</th>
                    
                </tr> 
            </table>
        </div>
        <div class="tickets-footer">
            <textarea  name="message" placeholder="輸入訊息" id="message_input" cols="88"></textarea>
            <button @click.prevent="changeTemplatePage" class="user-ticket-btn"><span>傳送</span></button>
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

            var url = 'https://ukbemjsll9.execute-api.us-east-2.amazonaws.com/test/api/ticket/content?ticket_id='
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
                console.log( data['data'] ) ;
                // this.myticket['ticketTitle'] = tickettitle ;
                // this.myticket['ticketCustomer'] = this.userdata['username']
                // this.myticket['createTime'] = data['data'][0]['created_at']
            })

        }
    },
    data() {
        return {
            myticket : {}
        }
    },
    mounted() {
        this.fetchTicket() ;
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
        background-color: #FDF5E6;
        display: flex ;
        flex-direction: row;
        position: relative ;
        width:80%;
        height: 30%;
        align-items: center ;
        margin: auto;
        /* border-top: 30px; */
       margin-bottom:3% ;
       margin-top: 3%;
        
    }
    .tickets-title table{
        width: 1000px;
        
    }
    /* .tickets-title table tr td{
        height: 50px ;
    } */
    
    .tickets-user-dialogue {
        background-color: #FDF5E6;
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
        background-color: rgb(202, 212, 166);
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
    .tickets-footer textarea{

        
        
    }
    .user-ticket-btn{
        display: inline-block;
        border-radius: 4px;
        background-color: rgb(153, 164, 112);
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