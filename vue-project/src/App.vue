<template>
    <section>
        <header-page></header-page>
        
        <section>
                <router-view  @loginSuccess="changeLoginStatus">

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
        'header-page' : header
    },
    provide() {
        return {
            UserName :  this.data['username']
        }
    },
    props : {
        
    },
    data() {
        return {
            data : {
                login : false,
                userrole : '',
                username : ''
            }
            
        }
        
    },
    methods : {
        check_login_status() {

            if ( this.login )
                return true ;
            else 
                return false ;
        },
        changeLoginStatus(status, name, role) {
            console.log( 'test1111111' ) ;
            if ( status != 'null') {
                this.data['login'] = true ;
                this.data['username'] = name ;
                this.data['userRole'] = role ;
                alert( this.data['username'] )
                this.UserName = this.data['username']
                console.log(this.UserName)
            }        
        }

    },
    mounted () {
        
        this.UserName = this.data['username']
        console.log(this.UserName)
    }
}
</script>

<style>

</style>