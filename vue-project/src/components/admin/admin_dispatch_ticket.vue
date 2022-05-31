<template>
    <div class="dispatch-table">
      <div class="dispatch-table-row1">
          <div class="dispatch-table-th1">ticket name</div>
          <div class="dispatch-table-th2">deadline</div>
          <div class="dispatch-table-th3">負責人</div>
           <div class="dispatch-table-th4"></div>
          
      </div>
      <div class="dispatch-table-row2">
          <div class="dispatch-table-td1">123456789101203488057534552344234241131423</div>
          <div class="dispatch-table-td2">2022/05/21</div>
          <div class="dispatch-table-td3"><select><option>請選擇負責人</option></select></div>
          <div class="dispatch-table-td4"><input value="Send" type="submit" /></div>

      </div>

        
    </div>
</template>

 <script>
 export default {
    data() {
        return {
            oneTicket : {}
        }
    },
    inject : [
        'userdata',
        'alltickets'
    ],
    methods : {

    }
 }
 </script>


<style>
.dispatch-table{
    display: table;
    position: relative;   
    width: 60%;
    height: 20%;
    left: 150px;
    top: 30px;
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
   width: 5%;

}
.dispatch-table .dispatch-table-row2{
     display: table-row; 
    
     table-layout: fixed;
     height: 10px;
     /* box-shadow: 0px 0px 9px 0px rgba(0, 0, 0, 0.1); */
}
.dispatch-table .dispatch-table-td1{
     display: table-cell;
     height: 10px;
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
     height: 10px;
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
     height: 10px;
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
     /* height: 10px;
      width: 10px; */
     text-align: center;
     vertical-align: middle;

}
input[type=submit]{
  margin-left: 10px;
  height: 120px;
  padding:10px 10px -10px 200px;
  font-size: 3em;
  font-weight: bold;
  font-family: "Open Sans";
  text-transform: uppercase;
  color: #696666;
  border-radius: 2em;
  border: 0.15em solid #F9C23C;
}
input[type="submit"]:hover {
    color: #fff;
    background-color: #EAA502;
    border-color: #EAA502;
    -webkit-transition: all 0.3s ease;
}



</style>