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
                    <th>問題內容:</th>
                    <td>yy/ds</td>
                </tr>
                    
                 
            </table>
        </div>
        <div class="tickets-thomas-dialogue">
            <table>
                <tr>
                    <th>(工程師名字)</th>
                </tr>
                <tr>
                    <th>回覆內容:</th>
                    <td>yy/ds</td>
                </tr>
            </table>
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



</style>