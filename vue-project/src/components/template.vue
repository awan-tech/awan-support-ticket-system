<template>
        <div class="template-content">
            <div class="template-left">
                <side-bar :Userdata="user"> </side-bar>
            </div>
            <div class="template-right">
                <router-view></router-view>
            </div>
            
        </div>

</template>


<script>
//:Userdata="userdata"
import sidebar from './sidebar.vue'
export default {
    props: {
        user: {
            type: Object,
        },
    },
    components : {
        'side-bar' : sidebar
    },
    inject: [],
    data() {
        return {
            status : false
        }
    },
    methods : {

    },
    computed: {
      
    },
}
</script>

<style>
    .template-content{
        /* background-color: rgb(10, 32, 25); */
        position: relative ;
        display: flex ;
        flex-direction: row ;
    }
    .template-left{
        
        position: relative ;
        display: flex ;
        flex-direction: row ;
    }
    .template-right{
        background-color: rgb(255, 255, 255);
        position: relative ;
        display: flex ;
        flex-direction: row ;
        width: 100%;
    }
    #sidebar {
    width: 250px;
    height: 100vh;
    background-color:#e5e5e5;
    color: #493D26;
    transition: 1s;
    float: left;
    position: relative;
    top: -8px;
    }
    #sidebar.active {
        margin-left: -200px;
    }
    .collapse-btn {
        position: relative;
        top: 1%;
        left: 200px;
        background-color: #e5e5e5d6;
        color: #1a1616cc;
        border: none;
        font-size: 30px;
        padding: 5px;
    }

    #collapse-btn:hover {
        background-color: rgba(77, 73, 73, 0.347);
        transition: 0.4s;
    }
    #sidebar ul li a {
        padding: 10px;
        font-size: 20px;
        display: block;
        text-decoration: none;
        color: rgb(29, 25, 25);
    }

    #sidebar ul li a:hover {
        color: rgb(255, 253, 253);
        background: rgb(153, 164, 112);
    }
    ul ul li a {
        background-color: rgb(153, 164, 112);
        font-size: 20px;
        font-style: italic;
    }
</style>