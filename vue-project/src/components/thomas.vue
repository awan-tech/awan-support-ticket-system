<template>
    <div>
        <div>
        <button id="pending-btn" onclick="連結">
            <div>
                <span>
                    <p>待處理:()件</p>
                </span>
            </div>
            <div>
                <span>
                    <p>上班加油</p><p>:D</p>
                </span>
            </div>
        </button> 
    </div>
    <div id="deadline-table">
        <div class="deadline-tr">
            <div class="deadline-td">公告</div>
            <div class="deadline-td">
                <div class="onoffswitch">
                    <input type="checkbox" name="onoffswitch" class="onoffswitch-checkbox" id="myonoffswitch" tabindex="0" checked>
                    <label class="onoffswitch-label" for="myonoffswitch">
                        <span class="onoffswitch-inner"></span>
                        <span class="onoffswitch-switch"></span>
                    </label>
                </div>
            </div>
        </div>
        <div class="deadline-tr">
            <div class="deadline-td">1231232113234343</div>
            <div class="deadline-td">987</div>
        </div>
        <div class="deadline-tr">
            <div class="deadline-td">123123234535</div>
            <div class="deadline-td">987</div>
        </div>
        <div class="deadline-tr">
            <div class="deadline-td">1231232325353543</div>
            <div class="deadline-td">987</div>
        </div>

    </div>

    </div>
</template>

<style>

#pending-btn {
    border: 0;
    display: flex;
    flex-direction: column;
    width: 100%;
    max-width: 140px;
    height: 50px;
    border-radius: 0.5em;
    overflow: hidden;
    position: relative;
    top: 50px;
    left: 100px;
   }
   
   #pending-btn div {
    transform: translateY(0px);
    width: 100%;
   }
   
   #pending-btn,
   #pending-btn div {
    transition: 0.6s cubic-bezier(.16,1,.3,1);
   }
   
   #pending-btn div span {
    display: flex;
    align-items: center;
    justify-content: space-between;
    height: 50px;
    padding: 0.75em 1.125em;
   }
   
   #pending-btn div:nth-child(1) {
    background-color: #1e90ff;
   }
   
   #pending-btn div:nth-child(2) {
    background-color: #21dc62;
   }
   
   #pending-btn:hover {
    box-shadow: 0 0.625em 1em 0 rgba(33, 220, 98, 0.35);
   }
   
   #pending-btn:hover div {
    transform: translateY(-50px);
   }
   
   #pending-btn p {
    font-size: 17px;
    font-weight: bold;
    color: #ffffff;
    
   }
   
   #pending-btn:active {
    transform: scale(0.95);
   }
   




   
#deadline-table {
    display:table;
    position: relative;
    top: 150px;
    left: 300px;
    border-collapse: collapse;
    font-weight: bold;

  }
  .deadline-tr {
    display: table-row;
    height: 30px;
  }
  .deadline-tr:nth-child(even) {
    background-color: #ccc;
  }
  .deadline-tr:nth-child(odd) {
    background-color: #fafafa;
  }
  .deadline-tr:hover {
    background-color: #E9CFEC;
  }


  .deadline-td {
      border:1px solid rgb(0, 0, 0);
      display: table-cell;
      width: auto;
      height: 100%;
      overflow: hidden;
      white-space: nowrap;
      background-color: #ffffff;
      text-align: center;
      vertical-align: middle;
      border-right: none;
      border-left: none;
      border-top: none;
  }
  

  .onoffswitch {
    position: relative; width: 93px;
    /* -webkit-user-select:none; -moz-user-select:none; -ms-user-select: none; */
}
.onoffswitch-checkbox {
    position: absolute;
    opacity: 0;
    pointer-events: none;
}
.onoffswitch-label {
    display: block; overflow: hidden; cursor: pointer;
    border: 2px solid #999999; border-radius: 0px;
}
.onoffswitch-inner {
    display: block; width: 200%; margin-left: -100%;
    transition: margin 0.3s ease-in 0s;
}
.onoffswitch-inner:before, .onoffswitch-inner:after {
    display: block; float: left; width: 50%; height: 25px; padding: 0; line-height: 25px;
    font-size: 14px; color: white; font-family: Trebuchet, Arial, sans-serif; font-weight: bold;
    box-sizing: border-box;
}
.onoffswitch-inner:before {
    content: "Deadline";
    padding-left: 5px;
    background-color: #34A7C1; color: #FFFFFF;
    text-align: left;
}
.onoffswitch-inner:after {
    content: "New";
    padding-right: 5px;
    background-color: #949494; color: #FFFFFF;
    text-align: right;
}
.onoffswitch-switch {
    display: block; width: 16px; margin: 4.5px;
    background: #FFFFFF;
    position: absolute; top: 0; bottom: 0;
    right: 64px;
    border: 2px solid #999999; border-radius: 18px;
    transition: all 0.3s ease-in 0s; 
}
.onoffswitch-checkbox:checked + .onoffswitch-label .onoffswitch-inner {
    margin-left: 0;
}
.onoffswitch-checkbox:checked + .onoffswitch-label .onoffswitch-switch {
    right: 0px; 
}
</style>