<template>
    <div class="user-myticket">
        <div class="user-myticket-left" >
            <button class="user-myticket-btn">
                <span>建單</span>
            </button>
        </div>
        <div class="user-myticket-right" >
            <div class="user-table">
                <li class="table-header">
                    <div class="user-table-tr">進行中</div>

                    <div class="user-table-tr">更新時間</div>
                </li>
                 <li class="table-row">
                     <div class="user-table-td1" data-label="Job Id">4223543556456435214246532438787548789385498689589328dbs796987ddddddddd</div>
                     
                     <div class="user-table-td2" data-label="Payment Status">Pending</div>
                </li>
                <li class="table-row">
                    <div class="user-table-td1" data-label="Job Id">42442</div>
                    
                    <div class="user-table-td2" data-label="Payment Status">Pending</div>
                </li>
                <li class="table-row">
                    <div class="user-table-td1" data-label="Job Id">42257</div>
                   
                    <div class="user-table-td2" data-label="Payment Status">Pending</div>
                </li>
                <li class="table-row">
                    <div class="user-table-td1" data-label="Job Id">42311</div>
            
                    <div class="user-table-td2" data-label="Payment Status">Pending</div>
                </li>   
                        
                </div>
        </div>
    </div>
    
    
</template>

<style>
    .user-table{
        position: relative;   
        width: 700px;
        left: -50px;
        top: 30px;
     /* padding-left: 10px;
     padding-right: 10px; */
        table-layout: fixed;
    }
    .user-table li{
        border-radius: 3px;
        padding: 25px 30px;
        display: flex;
        justify-content: space-between;
    }
    .user-table .table-header {
     background-color: #e5e5e5;
     font-size: 20px;
     font-weight: bolder;
     text-transform: uppercase;
     letter-spacing: 0.03em;
    }
     .user-table .table-row {
     background-color: #fff;
     box-shadow: 0px 0px 9px 0px rgba(0, 0, 0, 0.1);
    }
    .user-table .table-row:hover {
         background-color: rgb(153, 164, 112);
         color: rgb(255, 253, 253);
    }
     .user-table .user-table-tr {
         /* flex-basis: 10%; */
    }
    
    .user-table .user-table-td1 {
         flex-basis: 80%;
         overflow: hidden;
         text-overflow: ellipsis;
    }
    .user-table .user-table-td2 {
        flex-basis: 10%;
    }
  


    .user-myticket {
        width: 100%;
        position: relative ;
        display: flex ;
        
    }
    .user-myticket-left {
        /* background-color: rgb(105, 4, 4); */
        position: relative ;
        display: flex ;
        flex-direction: column ;
        width: 20%;
        align-items: center;
    }
    .user-myticket-right {
        /* background-color: aquamarine; */
        position: relative ;
        display: flex ;
        flex-direction: column ;
        width: 80%;
        align-items: center;
    }


    .user-myticket-btn {
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
        margin: 5px;
        position: relative;
        top: 30px;
        
        }

        .user-myticket-btn  span {
        cursor: pointer;
        display: inline-block;
        position: relative;
        transition: 0.5s;
        }

        .user-myticket-btn  span:after {
        content: '»';
        position: absolute;
        opacity: 0;
        top: 0;
        right: -15px;
        transition: 0.5s;
        }

        .user-myticket-btn:hover span {
        padding-right: 15px;
        }

        .user-myticket-btn:hover span:after {
        opacity: 1;
        right: 0;
        }
</style>