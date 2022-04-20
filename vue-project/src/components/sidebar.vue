<template>
    <nav id="sidebar">
        <button type="button" id="collapse" class="collapse-btn">
            <i class="fas fa-align-left"></i>
        </button>
        
        <ul class="list-unstyled">
            <div>
                <li>Hi,{{ Userdata['username'] }} </li>
            </div>
    
            <li>
                <router-link v-if="Userdata['userRole'] === 'customer'" to="/userhome">Home</router-link>
                <router-link v-else-if="Userdata['userRole'] === 'engineer'" to="/home">Home</router-link>
             
            </li>
            <li>
                <router-link v-if="Userdata['userRole'] === 'engineer'"  to="/home/tickets_table">Ticket</router-link>
                <router-link v-if="Userdata['userRole'] === 'customer'"  to="/userhome/tickets_table">Ticket</router-link>
                <!-- <ul v-if="myticketSublist" >
                    <li>
                        <router-link to="/home/tickets" > tickets </router-link>
                    </li>
                    <li>
                        <router-link to="/home/user_tickets" > user_tickets </router-link>
                    </li>
                </ul> -->
               
            </li>
            <li >
                <router-link v-if="Userdata['userRole'] === 'engineer'" to="/home/tickets" >History Ticket</router-link>
                <router-link v-if="Userdata['userRole'] === 'customer'" to="/userhome/tickets" >History Ticket</router-link>
            </li>
            <li>
                <router-link to="/home/settings">Setting</router-link>
            </li>
            <li v-if="Userdata['userRole'] === 'engineer' ">
                <router-link to="/home/manage" > Manager </router-link>
                <!-- <a href="#">Manager</a> -->
            </li>
            
            <li>
                <router-link to="/">Logout</router-link>
            </li>
        </ul>
    </nav>
</template>

<script>
export default {
    props: {
        Userdata: {
            type: Object,
        },
    },
    data() {
        return {
            myticketSublist : false,
            historySublist : false,
        }
    },
    methods: {
        toggleSublist() {
            this.myticketSublist = ! this.myticketSublist;
        },
        toggleMyTicketSublist() {
            this.historySublist = ! this.historySublist;
        },
        toTickets_table() {
            this.$router.push('tickets_table')
        },
        toTickets() {
            this.$router.push('tickets') ;
        },
    },
}
</script>


<style scoped>
    .template-content{
        /* background-color: rgb(10, 32, 25); */
        position: relative ;
        display: flex ;
        flex-direction: row ;
    }
    .template-left{
        
        position: relative ;
        display: flex ;
        flex-direction: row ;
    }
    .template-right{
        background-color: rgb(255, 255, 255);
        position: relative ;
        display: flex ;
        flex-direction: row ;
        width: 100%;
    }
    #sidebar {
    width: 250px;
    height: 100vh;
    background-color:#e5e5e5;
    color: #493D26;
    transition: 1s;
    float: left;
    position: relative;
    top: -8px;
    }
    #sidebar.active {
        margin-left: -200px;
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
    #sidebar ul li a {
        padding: 10px;
        font-size: 20px;
        display: block;
        text-decoration: none;
        color: rgb(29, 25, 25);
    }

    #sidebar ul li a:hover {
        color: rgb(255, 253, 253);
        background: rgb(153, 164, 112);
    }
    ul ul li a {
        font-size: 20px;
        font-style: italic;
    }
    .router-link-exact-active {
        background-color: rgb(153, 164, 112);
    }

    
</style>