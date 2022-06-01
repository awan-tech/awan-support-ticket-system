import { createApp } from 'vue';
import { createRouter, createWebHashHistory } from 'vue-router';
import App from './App.vue';
import BootstrapVue3 from "bootstrap-vue-3";

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue-3/dist/bootstrap-vue-3.css'
import login from './components/login.vue'
import template from './components/template.vue'
import thomas from './components/admin/thomas.vue'

import user_table from './components/user/user_table.vue'
import admin_tickets from './components/admin/admin_tickets.vue'
import create_form from './components/user/user_create_form.vue'
import settings from './components/setting.vue'
import manage from './components/admin/manage.vue'
import admin_tickets_table from './components/admin/admin_tickets_table.vue'
import user_tickets from './components/user/user_tickets.vue'
import user_tickets_table from './components/user/user_tickets_table.vue'
import admin_create_engineer from './components/admin/admin_create_engineer.vue'
import admin_dispatch_ticket from './components/admin/admin_dispatch_ticket'
import history_ticket from './components/admin/admin_history_ticket.vue'

const router = createRouter( {
    history : createWebHashHistory(process.env.BASE_URL ),
    routes: [
        {path: '/', component: login,alias: '/login' },
        
        {path: '/home', component: template, 
        props: (route) => route.params,
            children:[
                {
                    path : '',
                    component : thomas
                },
                {
                    path : 'tickets_table',
                    component : admin_tickets_table
                },
                {
                    path : 'tickets',
                    component : admin_tickets
                },
                {
                    path : 'history_ticket',
                    component : history_ticket
                },
                {
                    path : 'settings',
                    component : settings
                },
                {
                    path : 'manage',
                    component : manage
                },
                {
                    path: 'admin_create_engineer',
                    component : admin_create_engineer
                },
                {
                    path: 'admin_dispatch_ticket',
                    component : admin_dispatch_ticket
                }
            ]
        },
        {path: '/userhome', component: template, 
        props: (route) => route.params,
            children:[
                {
                    path : '',
                    component : user_table
                },
                {
                    path : 'tickets_table',
                    component : user_tickets_table
                },
                {
                    path : 'create_form',
                    component : create_form
                },
                {
                    path : 'tickets',
                    component : user_tickets
                },
                {
                    path : 'settings',
                    component : settings
                },
            ]
        },
        {path: '/NotFound(.*)', redirect:'/'}
    ]
})


const app = createApp(App);
app.use(BootstrapVue3);
app.use( router )

app.mount('#frameapp');
