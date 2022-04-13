<template>
        <div>
            <nav id="sidebar">
            
                <button type="button" id="collapse" class="collapse-btn">
                    <i class="fas fa-align-left"></i>
                </button>
                
                <ul class="list-unstyled">
                    <div>
                        <li>Hi,{{ userName }} </li>
                    </div>
               
                    <li>
                        <a href="#">Home</a>
                    </li>
                    <li>
                        <a href="#">My Ticket</a>
                    </li>
                    <li v-if="userRole !== 'customer' ">
                        <a @click="toggleSublist" >History Ticket</a>
                        <ul v-if="myticketSublist" id="sublist" class="list-unstyled collapse">
                            <li>
                                <a href="#">test</a>
                            </li>
                            <li>
                                <a href="#">test</a>
                            </li>
                            <li>
                                <a href="#">test</a>
                            </li>
                        </ul>
                    </li>
                    <li>
                        <a href="#">Setting</a>
                    </li>
                    <li v-if="role === 'manager' ">
                        <a href="#">Manager</a>
                    </li>
                    
                    <li>
                        <a href="#">Logout</a>
                    </li>
                </ul>

            </nav>
            <create-btn></create-btn>
            <user-table></user-table>
        </div>

</template>


<script>
export default {
    props:{
        userName : String,
        userRole : String
    },
    data() {
        return {
            myticketSublist : false
        }
    },
    methods : {
        toggleSublist() {
            this.myticketSublist = ! this.myticketSublist;
        }
    }
}

</script>

<style>
    #sidebar {
    width: 250px;
    height: 100vh;
    background-color:#e5e5e5;
    color: #c4c4c439;
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
        color: #c4c4c4cc;
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
        color: white;
    }

    #sidebar ul li a:hover {
        color: rgb(176, 175, 122);
        background: #fff;
    }
    ul ul li a {
        background-color: rgb(153, 164, 112);
        font-size: 20px;
        font-style: italic;
    }
</style>