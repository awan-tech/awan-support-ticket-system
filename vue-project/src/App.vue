<template>
    <div id="all">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <header-page id="headerup"></header-page>
        <div id="down">
                <router-view :user="data" @loginSuccess="changeLoginStatus" >

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
            all_tickets_page : this. temp_all_tickets_page,
            jwtToken : this.temp_JWTtoken
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
            tickets_page : '0',
            temp_all_tickets_page : {
                undo:0,
                doing:0,
                done:0
            },
            temp_JWTtoken : {jwt: ''}
        }
        
    },
    methods : {
        async getAllticket( jwt ) {
            let address = 'https://u7j2emffl8.execute-api.us-west-2.amazonaws.com/dev/api/tickets' ;
            let user_id = this.data['id'], role = this.data['userRole'] ;
            // console.log( address + '?page=' + this.tickets_page + '&status=not processed' + '&user_id=' + user_id + '&role=' + role )
            // console.log('jwt' )
            // console.log( jwt )
            await fetch( address + '?page=' + String(this.tickets_page)  + '&status=not processed' + '&user_id=' + user_id + '&role=' + role ,{
            method: 'GET',
            headers : {
                'Content-Type': 'application/json',
                'Authorization' : jwt,
            },
            })
            .then( (response) => {
                if ( response.ok ) {
                    return response.json() ;
                }
            })
            .catch((err) =>{
                console.log(err)
            })
            .then((data) => { 
                console.log ('undo')
                console.log( data['data'] ) ;
                this.fetchalltickets['undo'] = data['data'] ;
                this.temp_all_tickets_page['undo'] = data['total_page']
            })
            

            await fetch( address + '?page=' + String(this.tickets_page)  + '&status=processing' + '&user_id=' + user_id + '&role=' + role ,{
            method: 'GET',
            headers : {
                'Content-Type': 'application/json',
                'Authorization' : jwt
            },
            })
            .then( (response) => {
                if ( response.ok ) {
                    return response.json() ;
                }
            })
            .catch((err) =>{
                console.log(err)
            })
            .then((data) => { 
                console.log ('doing')
                console.log( data ) ;
                this.fetchalltickets['doing'] = data['data'] ;
                this.temp_all_tickets_page['doing'] = data['total_page']
            })
            
            fetch( address + '?page=' + String(this.tickets_page)  + '&status=processed' + '&user_id=' + user_id + '&role=' + role ,{
            method: 'GET',
            headers : {
                'Content-Type': 'application/json',
                'Authorization' : jwt
            },
            })
            .then( (response) => {
                if ( response.ok ) {
                    return response.json() ;
                }
            })
            .catch((err) =>{
                console.log(err)
            })
            .then((data) => { 
                console.log ('done')
                this.fetchalltickets['done'] = data['data'] ;
                this.temp_all_tickets_page['done'] = data['total_page']
            })
            
            
            await this.concatTickets() ;
        },
        async changeLoginStatus(id, name, role) {
            
            if ( id != 'null') {
                await this.change_user(id, name, role)
                // this.data['id'] = id ;
                // this.data['username'] = name ;
                // this.data['userRole'] = role ;
                const userObj = await Auth.currentSession() ;
                
                this.temp_JWTtoken.jwt = userObj['idToken']['jwtToken'] 
                // console.log( 'test', this.temp_JWTtoken )
                await this.getAllticket( this.temp_JWTtoken.jwt  ) ;
            }        
        },
        change_user( id, name, role) {
            this.data['id'] = id ;
            this.data['username'] = name ;
            this.data['userRole'] = role ;
        },
        async getLoginStatus() {
            try {
                
                const user = await Auth.currentUserInfo(); 
                if ( user != null ) {
                    console.log( 'login success')
                    await  this.changeLoginStatus( user['attributes']['custom:id'], user['attributes']['custom:name'], user['attributes']['custom:role'] )
                    // this.temp_JWTtoken = await Auth.currentSession()['idToken']['jwtToken']  ;
                    
                    //  console.log( Auth.currentSession()['idToken']) 
                    // console.log( 'getlogin', this.temp_JWTtoken ) 
                    // console.log( userObj['idToken']['jwtToken'] ) ;
                    // await this.getAllticket( this.temp_JWTtoken  ) ;
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
        change_page( action, page ) {
            console.log('change page')
            if ( action === 'jump') {
                this.tickets_page = Number(page)  ;
            }
            else if ( action === 'add' ) {
                this.tickets_page += 1 ;
            }
            else if ( action === 'sub' ) {
                this.tickets_page -= 1 ;
            }
        }
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