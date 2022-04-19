<template>
    <section>
        <header-page></header-page>
        
        <section>
                <router-view :user="data" @loginSuccess="changeLoginStatus">

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
    data() {
        return {
            data : {
                login : false,
                userRole : '',
                username : ''
            }
            
        }
        
    },
    methods : {
        changeLoginStatus(status, name, role) {
            console.log( 'test1111111' ) ;
            if ( status != 'null') {
                this.data['login'] = true ;
                this.data['username'] = name ;
                this.data['userRole'] = role ;
            }        
        }
    }
}
</script>

<style>

</style>