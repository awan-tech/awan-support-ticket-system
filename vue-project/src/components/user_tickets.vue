<template>
    <div id="tickets-content">
        <div class="tickets-title">
            <table>
                <tr>
                    <td>
                        ticketname:
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
        background-color: #ffffff;
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
       font-weight: bolder;
       font-size: 20px;
        
    }
    .tickets-title table{
        width: 1000px;
        
    }
    /* .tickets-title table tr td{
        height: 50px ;
    } */
    
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
    .tickets-footer textarea{

        
        
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