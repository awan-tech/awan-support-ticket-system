<template>
    <div id="all">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <header-page id="headerup"></header-page>
        <div id="down">
                <router-view :user="data" @loginSuccess="changeLoginStatus">

                </router-view>
        </div>
        
    </div>
    
    
</template>


<script>
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
    #all{
        position: relative ;
        display: flex ;
        flex-direction: column;
        height: 100%;
        width: 100%;
    }
    #headerup{
        position: relative ;
        display: flex ;
        flex-direction: column;
        text-align:center;
        align-items: center;
        height: 20%;
      
    }
    #down{
        position: relative ;
        display: flex ;
        flex-direction: column;
        height: 100vh;
        width: 100%;
    }

</style>