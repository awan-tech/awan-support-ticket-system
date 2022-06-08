<template>
        <div class="template-content">
            <div class="template-left">
                <side-bar :Userdata="user" @redirect_home="againgetticket()" > </side-bar>
            </div>
            <div class="template-right">
                <router-view @all_ticket_contents="transferTicketId"></router-view>
            </div>
            
        </div>

</template>


<script>
// import { Auth } from "aws-amplify";
import sidebar from './sidebar.vue'
export default {
    props: {
        user: {
            type: Object,
        },
    },
    inject : [
        'alltickets',
        'ticketcontent'
    ],
    provide(){
        return {
        //   alltickets: this.fetchalltickets,
          ticketcontent : this.oneTicket // for user_tickets and admin_tickets from user_table
        }
    },
    components : {
        'side-bar' : sidebar
    },
    data() {
        return {
            status : false,
            all_tickets_content : { topics: [ '123']},
            fetchalltickets : {},
            oneTicket : {},
            tickets_page : '0'
        }
    },
    methods : {
        async getAllticket() {
            let address = 'https://kdmm5wrtrb.execute-api.us-west-2.amazonaws.com/dev/api/tickets' ;
            let user_id = this.user['id'], role = this.user['userRole'] ;
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
            // body :  JSON.stringify({
            //     "user_id": this.user['id'],
            //     "role": this.user['userRole']
            // })
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
        concatTickets() {
            this.fetchalltickets['customer_doing'] = this.fetchalltickets['doing']
            this.fetchalltickets['customer_doing'] = this.fetchalltickets['customer_doing'] .concat( this.fetchalltickets['undo'])
            this.fetchalltickets['customer_doing'] = this.fetchalltickets['customer_doing'].sort(function(a,b) {
                return a.ticket_id > b.ticket_id ? 1 : -1;
            })

        },
        transferTicketId( ticketid, tickettitle, ticket_admin_name) {
            this.oneTicket['ticketid'] = ticketid ;
            this.oneTicket['title'] = tickettitle ;
            this.oneTicket['admin_name'] = ticket_admin_name ;
        },
        againgetticket() {
            console.log('reload tickets')
            // this.$router.go(0)
            this.getAllticket()
        },
        change_page( page ) {
            this.tickets_page = page ;
            // this.getAllticket() ;
        }
    },
    created() {
        // this.getAllticket() ;
        // this.isUserSignIn() ;
    },
}
</script>

<style>
    .template-content{
        
        position: relative ;
        display: flex ;
        flex-direction: row ;
        overflow:auto;
        height: 120%;
        
    }
    .template-left{
        position: relative ;
        display: flex ;
        flex-direction: row ;
        background-color: #e5e5e5;
        height: 100%;
        
    }
    .template-right{
        position: relative ;
        display: flex ;
        flex-direction: row ;
        width: 100%;
        overflow:auto;

        background:url(../../public/background.png);
        
    }

    .collapse-btn {
        position: relative;
        top: 1%;
        left: 200px;
        background-color: #e5e5e5d6;
        color: #1a1616cc;
        border: none;
        font-size: 30px;
        padding: 5px;
    }

    #collapse-btn:hover {
        background-color: rgba(77, 73, 73, 0.347);
        transition: 0.4s;
    }
    .template-right background {
        z-index:1;
        
    }
</style>
