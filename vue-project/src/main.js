import { createApp } from 'vue';
import { createRouter, createWebHistory } from 'vue-router';
import App from './App.vue';
import BootstrapVue3 from "bootstrap-vue-3";

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue-3/dist/bootstrap-vue-3.css'
import login from './components/login.vue'
import template from './components/template.vue'
import thomas from './components/thomas.vue'

const router = createRouter( {
    history: createWebHistory(),
    routes: [
        {path: '/', component: login },
        {path: '/home', component: template },
        {path: '/myticket', component: thomas }
    ]
})

const app = createApp(App);
app.use(BootstrapVue3);
app.use( router )

app.mount('#frameapp');
