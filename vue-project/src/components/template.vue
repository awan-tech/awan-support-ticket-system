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
//:Userdata="userdata"
import sidebar from './sidebar.vue'
export default {
    props: {
        user: {
            type: Object,
        },
    },
    provide(){
        return {
          userdata : this.all_tickets_content,
          alltickets: this.fetchalltickets,
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
            oneTicket : {}
        }
    },
    methods : {
        getAllticket() {
            let address = 'https://kdmm5wrtrb.execute-api.us-west-2.amazonaws.com/dev/api/tickets' ;
            let page = '0', user_id = this.user['id'], role = this.user['userRole'] ;
            console.log( address + '?page=' + page + '&status=not processed' + '&user_id=' + user_id + '&role=' + role )
            fetch( address + '?page=' + page + '&status=not processed' + '&user_id=' + user_id + '&role=' + role ,{
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

            fetch( address + '?page=' + page + '&status=processing' + '&user_id=' + user_id + '&role=' + role ,{
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

            fetch( address + '?page=' + page + '&status=processed' + '&user_id=' + user_id + '&role=' + role ,{
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
                console.log( data['data'] ) ;
                this.fetchalltickets['done'] = data['data'] ;
            })
        },
        transferTicketId( ticketid, tickettitle, ticket_admin_name) {
            this.oneTicket['ticketid'] = ticketid ;
            this.oneTicket['title'] = tickettitle ;
            this.oneTicket['admin_name'] = ticket_admin_name ;
        },
        againgetticket() {
            console.log('reload tickets')
            this.getAllticket()
        }
    },
    mounted() {
        this.getAllticket()
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
