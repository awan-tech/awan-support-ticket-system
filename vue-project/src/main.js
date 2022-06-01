import { createApp } from 'vue';
import { createRouter, createWebHashHistory } from 'vue-router';
import App from './App.vue';
import BootstrapVue3 from "bootstrap-vue-3";

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue-3/dist/bootstrap-vue-3.css'
import login from './components/login.vue'
import template from './components/template.vue'
import thomas from './components/thomas.vue'

import user_table from './components/user_table.vue'
import admin_tickets from './components/admin_tickets.vue'
import create_form from './components/user_create_form.vue'
import settings from './components/setting.vue'
import manage from './components/manage.vue'
import admin_tickets_table from './components/admin_tickets_table.vue'
import user_tickets from './components/user_tickets.vue'
import user_tickets_table from './components/user_tickets_table.vue'

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
                    path : 'settings',
                    component : settings
                },
                {
                    path : 'manage',
                    component : manage
                },
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
