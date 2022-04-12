<template>
    <section>
        <header-page></header-page>


        <section>
            <login-page v-if="!check_login_status()"></login-page>
            <template-page v-else></template-page>
        </section>
        
    </section>
    
</template>


<script>
export default {
    props : {

    },
    data() {
        return {
            login : false,
            role : ''
        }
        
    },
    methods : {
        check_login_status() {
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