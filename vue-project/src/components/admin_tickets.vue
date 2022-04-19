<template>
    <div id="tickets-content">
        <div class="tickets-title">
            <table>
                <tr>
                    <td>
                        ticketname:
                    </td>
                    <td>
                        deadline:
                    </td>
                </tr>
                <tr>
                    <td>
                        customrname:
                    </td>
                    <td>
                        負責人:
                    </td>
                </tr>
                <tr>
                    <td>
                        time:
                    </td>
                    <td>
                        緊急程度:
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
                    <th>回覆內容: {{ userdata }}</th>
                    
                </tr> 
            </table>
        </div>
        <div class="tickets-footer">
            <textarea  name="message" placeholder="輸入訊息" id="message_input" cols="88"></textarea>
            <button>傳送</button>
        </div>
    </div>
</template>

<script>
export default {
    props : [
        'ticket'
    ],
    inject : [
        'userdata'
    ],
    data() {
        return {
            data: {
                TicketTitle : 'i want to ask',
                Deadline : '03/26 15:56:02',
                CustomerName : 'Daniel',
                Engineer : 'Larry',
                CreatedTime : '03/25 15:56:02'
            }
        }
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
        position: absolute;
        left:   100px;
        top: 500px;
        
        
    }
    .tickets-footer textarea{

        
        
    }
    .tickets-footer button{
        color: #090909;
        padding: 0.7em 1.7em;
        font-size: 18px;
        border-radius: 0.5em;
        background: #e8e8e8;
        border: 1px solid #e8e8e8;
        transition: all .3s;
        box-shadow: 6px 6px 12px #c5c5c5,
        -6px -6px 12px #ffffff;
        position: relative;
        
        left: 720px;

    }
    .tickets-footer button:hover {
        border: 1px solid white;
    }
    .tickets-footer button:active {
         box-shadow: 4px 4px 12px #c5c5c5,
        -4px -4px 12px #ffffff;
    }


</style>