<template>
    <section>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
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
    provide(){
        return {
          userlogindata : this.data 
        }
    },
    components : {
        'header-page' : header
    },
    data() {
        return {
            data : {
                id : '',
                userRole : '',
                username : ''
            }
            
        }
        
    },
    methods : {
        changeLoginStatus(id, name, role) {
            console.log( 'test1111111' ) ;
            if ( id != 'null') {
                this.data['id'] = id ;
                this.data['username'] = name ;
                this.data['userRole'] = role ;
            }        
        }
    }
}
</script>

<style>


</style>