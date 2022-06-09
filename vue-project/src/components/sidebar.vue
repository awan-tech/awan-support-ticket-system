<template>
    <nav id="sidebar">
        
        <ul class="list-unstyled">
            <div>
                <li>Hi, {{ Userdata['username'] }},  {{ Userdata['userRole'] }} </li>
            </div>
    
            <li>
                <a v-if="Userdata['userRole'] === 'Engineer Supervisor'" href="#/home" @click="make_redirect">Home</a>
                <a v-else-if="Userdata['userRole'] === 'Engineer'" href="#/home" @click="make_redirect">Home</a>
                <a v-else href="#/userhome" @click="make_redirect"> Home</a>
             
            </li>
            <li>
                <router-link v-if="Userdata['userRole'] === 'Engineer'"  to="/home/tickets_table">Ticket</router-link>
                <router-link v-else-if="Userdata['userRole'] === 'Engineer Supervisor'"  to="/home/tickets_table">Ticket</router-link>
                <router-link v-else  to="/userhome/tickets_table">Ticket</router-link>
                
               
            </li>
            <li >
                <router-link v-if="Userdata['userRole'] === 'Engineer'" to="/home/history_ticket" >History Ticket</router-link>
                <router-link v-else-if="Userdata['userRole'] === 'Engineer Supervisor'" to="/home/history_ticket" >History Ticket</router-link>
                <!-- <router-link v-else to="/userhome/tickets" >History Ticket</router-link> -->
            </li>
            <li>
                <router-link to="/home/settings">Setting</router-link>
            </li>
            <li v-if="Userdata['userRole'] === 'Engineer Supervisor' ">
                <a @click="toggle_myticketSublist">Manager</a>
                <!-- <router-link to="/home/manage" > Manager </router-link> -->
                <ul v-if="myticketSublist"  >
                    <!-- <li>
                        <router-link to="/home/admin_create_engineer" > 更改Engineer 資料  </router-link>
                    </li> -->
                    <li>
                        <router-link to="/home/admin_dispatch_ticket" style="font-size:15px" > 分派tickets </router-link>
                    </li>
                    <li>
                        <router-link to="/home/admin_create_engineer" style="font-size:15px"  > 新增Engineer帳號 </router-link>
                    </li>
                </ul>
                
            </li>
            
            <li>
                <router-link to="/" @click="logout">Logout</router-link>
            </li>
        </ul>
    </nav>
</template>

<script>
import { Auth } from "aws-amplify";
export default {
    emits:[
        'redirect_home'
    ],
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
        toTickets_table() {
            this.$router.push('tickets_table')
        },
        toTickets() {
            this.$router.push('tickets') ;
        },
        make_redirect() {
            this.$emit( 'redirect_home' )
            this.$router.push('/userhome') ;
        },
        toggle_myticketSublist() {
            this.myticketSublist = ! this.myticketSublist ;
        },
        logout() {
            Auth.signOut() ;
        }
        
    },
}
</script>


<style scoped>
    #sidebar {
    width: 160px;
    height: 100vh;
    background-color:#e5e5e5;
    color: #493D26;
    transition: 1s;
    float: left;
    position: relative;
    text-align: center;
    }
    #sidebar.active {
        margin-left: -200px;
    }
   

  
    #sidebar ul li a {
        padding: 10px;
        font-size: 17px;
        display: block;
        text-decoration: none;
        color: rgb(29, 25, 25);
    }

    #sidebar ul li a:hover {
        color: rgb(255, 253, 253);
        background: #797979;
    }
    ul ul li a {
        font-size: 20px;
        font-style: italic;
    }
    .router-link-exact-active {
        background-color: #797979;
    }
    .list-unstyled li{
        height: 10%;
    }
    
</style>