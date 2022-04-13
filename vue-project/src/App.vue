<template>
    <section>
        <header-page></header-page>


        <section>
            <login-page v-if="!check_login_status()"></login-page>
            <template-page v-else></template-page>
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
            login : true,
            role : ''
        }
        
    },
    methods : {
        check_login_status() {

        // axios.get('https://11931uvt3a.execute-api.us-east-2.amazonaws.com/test/helloworld')
        // .then(function (response) {
        //     // handle success
        //     console.log(response);
        // })
        // .catch(function (error) {
        //     // handle error
        //     console.log(error);
        // })
        // .then(function (data ) {
        //     console.log('test' + data )
        //     // always executed
        // });


            fetch('https://11931uvt3a.execute-api.us-east-2.amazonaws.com/test/helloworld',{
                method: 'GET',
                mode : 'no-cors',
                credentials: "include"
                })
            .then( (response) => {
                if ( response.ok ) {
                    return response.json() ;
                }
            })
            .then((data) => {
                
                console.log( 'test' + data ) ;
                    
            })

            if ( this.login )
                return true ;
            else 
                return false ;
        }
    }
}
</script>

<style>

</style>