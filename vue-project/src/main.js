import { createApp } from 'vue';
import { createRouter, createWebHistory } from 'vue-router';
import App from './App.vue';
import BootstrapVue3 from "bootstrap-vue-3";

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue-3/dist/bootstrap-vue-3.css'
import login from './components/login.vue'
import template from './components/template.vue'
import thomas from './components/thomas.vue'

import user_table from './components/user_table.vue'
import tickets from './components/tickets.vue'
import create_form from './components/user_create_form.vue'
import settings from './components/setting.vue'

const router = createRouter( {
    history: createWebHistory(),
    routes: [
        {path: '/', component: login,alias: '/login', props: (route) => route.params },
        
        {path: '/home', component: template,
            children:[
                {
                    path : '',
                    component : thomas
                },
                {
                    path : 'tickets',
                    component : tickets
                },
                {
                    path : 'user_table',
                    component : user_table
                },
                {
                    path : 'create_form',
                    component : create_form
                },
                {
                    path : 'settings',
                    component : settings
                },

            ]
        },
        {path: '/myticket', component: settings },
        {path: '/NotFound(.*)', redirect:'/'}
    ]
})

const app = createApp(App);
app.use(BootstrapVue3);
app.use( router )

app.mount('#frameapp');
