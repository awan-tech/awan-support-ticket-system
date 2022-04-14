<template>
    <div class="user-myticket">
        <div class="user-myticket-left" >
            <button class="user-myticket-btn">
                <span>建單</span>
            </button>
        </div>
        <div class="user-myticket-right" >
            <table class="test-table">
                <tr>
                    <td>國家</td>
                    <td>首都</td>
                    <td>人口</td>
                    <td>語言</td>
                </tr>
                <tr>
                    <td>USA</td>
                    <td>Washington D.C.</td>
                    <td>309 million</td>
                    <td>English</td>
                </tr>
                <tr>
                    <td>Sweden</td>
                    <td>Stockholm</td>
                    <td>9 million</td>
                    <td>Swedish</td>
                </tr>
            </table>
        </div>
    </div>
    
    
</template>

<style>
    .test-table{
        background-color: grey ;
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

        .user-myticket-btn :hover span {
        padding-right: 15px;
        }

        .user-myticket-btn :hover span:after {
        opacity: 1;
        right: 0;
        }
</style>