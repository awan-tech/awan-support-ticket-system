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