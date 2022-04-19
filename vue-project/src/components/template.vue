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
            status : false,
            all_tickets_content : {}
        }
    },
    methods : {
        getAllticket() {
            fetch('https://mbsgp811h1.execute-api.us-east-2.amazonaws.com/test/helloworld',{
            method: 'GET',
            headers : {
                'Content-Type': 'application/json'
            },
            // body :  JSON.stringify({
            //   name : 'Larry'
            // })
            })
            .then( (response) => {
                if ( response.ok ) {
                    return response.json() ;
                }
            })
            .then((data) => { 
                this.checkuser = data['name'] ;
                this.checkpassword = data['password'] ;
                this.role = data['role'] ;
                this.loginstatus() ;
            })
        }
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
</style>