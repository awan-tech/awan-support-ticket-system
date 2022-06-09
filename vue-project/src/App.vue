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
import { Auth } from "aws-amplify";
export default {
    provide(){
        return {
            userlogindata : this.data,
            alltickets: this.fetchalltickets,
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
            },
            fetchalltickets : {},
            tickets_page : '0'
        }
        
    },
    methods : {
        async getAllticket() {
            let address = 'https://kdmm5wrtrb.execute-api.us-west-2.amazonaws.com/dev/api/tickets' ;
            let user_id = this.data['id'], role = this.data['userRole'] ;
            // console.log( address + '?page=' + this.tickets_page + '&status=not processed' + '&user_id=' + user_id + '&role=' + role )

            await fetch( address + '?page=' + this.tickets_page + '&status=not processed' + '&user_id=' + user_id + '&role=' + role ,{
            method: 'GET',
            headers : {
                'Content-Type': 'application/json'
            },
            })
            .then( (response) => {
                if ( response.ok ) {
                    return response.json() ;
                }
            })
            .then((data) => { 
                console.log ('undo')
                console.log( data['data'] ) ;
                this.fetchalltickets['undo'] = data['data'] ;
            })

            await fetch( address + '?page=' + this.tickets_page + '&status=processing' + '&user_id=' + user_id + '&role=' + role ,{
            method: 'GET',
            headers : {
                'Content-Type': 'application/json'
            },
            })
            .then( (response) => {
                if ( response.ok ) {
                    return response.json() ;
                }
            })
            .then((data) => { 
                console.log ('doing')
                console.log( data['data'] ) ;
                this.fetchalltickets['doing'] = data['data'] ;
            })

            fetch( address + '?page=' + this.tickets_page + '&status=processed' + '&user_id=' + user_id + '&role=' + role ,{
            method: 'GET',
            headers : {
                'Content-Type': 'application/json'
            },
            })
            .then( (response) => {
                if ( response.ok ) {
                    return response.json() ;
                }
            })
            .then((data) => { 
                console.log ('done')
                this.fetchalltickets['done'] = data['data'] ;
            })
            
            await this.concatTickets() ;
        },
        async changeLoginStatus(id, name, role) {
            
            if ( id != 'null') {
                await this.change_user(id, name, role)
                // this.data['id'] = id ;
                // this.data['username'] = name ;
                // this.data['userRole'] = role ;
                await this.getAllticket() ;
            }        
        },
        change_user( id, name, role) {
            this.data['id'] = id ;
            this.data['username'] = name ;
            this.data['userRole'] = role ;
        },
        async getLoginStatus() {
            try {
                // const userObj = await Auth.currentSession() ;
                // console.log( userObj ) ;
                const user = await Auth.currentUserInfo(); 
                if ( user != null ) {
                    await  this.changeLoginStatus( user['attributes']['custom:id'], user['attributes']['custom:name'], user['attributes']['custom:role'] )
                    // this.data['id'] = user['attributes']['custom:id'];
                    // this.data['username'] = user['attributes']['custom:name'] ;
                    // this.data['userRole'] = user['attributes']['custom:role'] ;
                    console.log( 'login success')
                    // await this.getAllticket() ;
                }
                else {
                    console.log( 'no attribute')
                }
            }
            catch(err) {
                console.log( err )
            }
        },
        concatTickets() {
            this.fetchalltickets['customer_doing'] = this.fetchalltickets['doing']
            this.fetchalltickets['customer_doing'] = this.fetchalltickets['customer_doing'] .concat( this.fetchalltickets['undo'])
            this.fetchalltickets['customer_doing'] = this.fetchalltickets['customer_doing'].sort(function(a,b) {
                return a.ticket_id > b.ticket_id ? 1 : -1;
            })

        },
    },
    created() {
        this.getLoginStatus() ;
        // this.getAllticket() ;
    },
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