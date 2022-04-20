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
    provide(){
        return {
          userdata : this.all_tickets_content 
        }
    },
    components : {
        'side-bar' : sidebar
    },
    data() {
        return {
            status : false,
            all_tickets_content : { topics: [ '123']}
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
                // this.all_tickets_content = data;
                this.all_tickets_content['tickets'] = data['data'] 
                console.log(this.all_tickets_content)

            })
        }
    },
    mounted() {
        this.getAllticket()
    },
    computed: {
        
    }
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
        /* background-color: rgb(255, 255, 255); */
        position: relative ;
        display: flex ;
        flex-direction: row ;
        width: 100%;
        background:url(../../public/background.png);
        
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
    .template-right background {
        z-index:1;
        
    }
    /* .template-right route-view{
        position: relative;
        z-index: 10;
    } */
</style>
