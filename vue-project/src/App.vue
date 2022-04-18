<template>
    <section>
        <header-page></header-page>
        
        <section>
                <router-view>

                </router-view>
        </section>
        
    </section>
    
</template>


<script>
// const axios = require('axios'); 
// import login from './components/login.vue'
// import template from './components/template.vue'
import header from './components/header.vue'

export default {
    components : {
        // 'login-page' : login,
        // 'template-page' : template,
        'header-page' : header
    },
    props : {
        
    },
    data() {
        return {
            login : false,
            userrole : '',
            username : ''
        }
        
    },
    methods : {
        check_login_status() {

            // fetch('https://11931uvt3a.execute-api.us-east-2.amazonaws.com/test/helloworld',{
            //     method: 'GET',
            //     headers : {
            //         'Content-Type': 'application/json'
            //         //'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'
            //     },
            //     })
            // .then( (response) => {
            //     if ( response.ok ) {
            //         return response.json() ;
            //     }
            // })
            // .then((data) => {
            //     console.log(  data['name'] ) ; 
            // })

            if ( this.login )
                return true ;
            else 
                return false ;
        },
        

    }
}
</script>

<style>

</style>