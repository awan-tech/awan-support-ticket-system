<template>
        <div class="template-content">
            <div class="template-left">
                <nav id="sidebar">
                    <button type="button" id="collapse" class="collapse-btn">
                        <i class="fas fa-align-left"></i>
                    </button>
                    
                    <ul class="list-unstyled">
                        <div>
                            <li>Hi,{{ userName }} </li>
                        </div>
                
                        <li>
                            <a @click="selectpage('thomas-page')">Home</a>
                        </li>
                        <li>
                            <a @mouseenter="myticketSublist = true" @mouseleave="myticketSublist = false" @click="selectpage('user-table')" >My Ticket</a>
                            <ul v-if="myticketSublist" @mouseenter="myticketSublist = true" @mouseleave="myticketSublist = false">
                                <li @click="selectpage('tickets-page')">
                                    <a>ticket</a>
                                </li>
                            </ul>
                        </li>
                        <li v-if="userRole !== 'customer' ">
                            <a @mouseenter="historySublist = true" @mouseleave="historySublist = false"  >History Ticket</a>
                            <ul v-if="historySublist" @mouseenter="historySublist = true" @mouseleave="historySublist = false">
                                <li>
                                    <a>test1</a>
                                </li>
                                <li>
                                    <a>test2</a>
                                </li>
                                
                            </ul>
                        </li>
                        <li @click="selectpage('setting-page')">
                            <a >Setting</a>
                        </li>
                        <li v-if="userRole === 'manager' ">
                            <a href="#">Manager</a>
                        </li>
                        
                        <li>
                            <a href="#">Logout</a>
                        </li>
                    </ul>
                </nav>
            </div>
            <div class="template-right">

                <user-table v-if="which_page === 'user-table'" @changepage="changeToCreateForm"></user-table>
                <tickets-page v-if="which_page === 'tickets-page'"></tickets-page>
                <create-form-page v-if="which_page === 'create-form-page'"></create-form-page>
                <thomas-page v-if="which_page === 'thomas-page'"></thomas-page>
                <setting-page v-if="which_page === 'setting-page'"></setting-page>
            </div>
            
        </div>

</template>


<script>
import user_table from './user_table.vue'
import tickets from './tickets.vue'
import create_form from './user_create_form.vue'
import thomas from './thomas.vue'
import settings from './setting.vue'

export default {
    components : {
      'user-table' : user_table,
      'tickets-page' : tickets,
      'create-form-page': create_form,  
      'thomas-page' : thomas,
      'setting-page' : settings 

    },
    props:{
        userName : String,
        userRole : String
    },
    data() {
        return {
            myticketSublist : false,
            historySublist : false,
            which_page : 'tickets-page'
        }
    },
    methods : {
        toggleSublist() {
            this.myticketSublist = ! this.myticketSublist;
        },
        toggleMyTicketSublist() {
            this.historySublist = ! this.historySublist;
        },
        selectpage( pagename) {
            this.which_page=pagename ;
        },
        changeToCreateForm( pagename ) {
            this.which_page = pagename ;
        }

    }
}

</script>

<style>
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
        background-color: rgb(153, 164, 112);
        font-size: 20px;
        font-style: italic;
    }
</style>