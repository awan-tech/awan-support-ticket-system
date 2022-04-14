<template>
    <div class="tickets-content">
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
        <div class="tickets-dialogue">
            message
        </div>
    </div>
</template>

<script>
export default {
    
}
</script>

<style>
    .tickets-content{
        /* background-color: gray ; */
        width: 100%;
        position: relative ;
    }
    .tickets-title {
        background-color: aquamarine;
        display: flex ;
        flex-direction: row;
        position: relative ;
        width:80%;
        height: 30%;
        align-items: center ;
        margin: auto;
        /* border-top: 30px; */
        
    }
    .tickets-title table{
        width: 1000px;
        
    }
    .tickets-title table tr td{
        height: 50px ;
    }
    
    .tickets-dialogue {
        background-color: yellow;
        display: flex ;
        flex-direction: row;
        position: relative ;
        width: 80%;
        height: 20%;
        margin: auto;  
        align-items: center ;
    }


</style>