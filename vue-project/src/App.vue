<template>
    <section>
        <header-page></header-page>


        <section>
            <login-page v-if="!check_login_status()"
                @loginSuccess="changeLoginStatus"
            ></login-page>
            <template-page v-else
                :user-name="username"
                :user-role="userrole"
            ></template-page>
            <!-- <create-btn></create-btn> -->
        </section>
        
    </section>
    
</template>


<script>
// const axios = require('axios'); 

export default {
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
        changeLoginStatus(status, name, role) {
            if ( status != 'null') {
                this.login = true ;
                this.username = name ;
                this.userrole = role ;
            }
                
        }

    }
}
</script>

<style>

</style>