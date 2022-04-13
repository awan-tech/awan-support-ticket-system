<template>
<div>
    <button>
        <span>建單</span>
    </button>
</div>
</template>

<style>
/* From uiverse.io by @NorthFishHasNa */
button {
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
 top: 100px;
 left: 80px;
}

button span {
 cursor: pointer;
 display: inline-block;
 position: relative;
 transition: 0.5s;
}

button span:after {
 content: '»';
 position: absolute;
 opacity: 0;
 top: 0;
 right: -15px;
 transition: 0.5s;
}

button:hover span {
 padding-right: 15px;
}

button:hover span:after {
 opacity: 1;
 right: 0;
}

</style>