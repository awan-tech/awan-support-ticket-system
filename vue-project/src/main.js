import { createApp } from 'vue';
import App from './App.vue';
import login from './components/login.vue'
import template from './components/template.vue'
import header from './components/header.vue'
import create_btn from './components/create_btn.vue'
import user_table from './components/user_table.vue'
import BootstrapVue3 from "bootstrap-vue-3";

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue-3/dist/bootstrap-vue-3.css'


const app = createApp(App);
app.use(BootstrapVue3);
app.component('header-page', header ) ;
app.component( 'login-page', login ) ;
app.component('template-page', template ) ;
app.component('create-btn', create_btn);
app.component('user-table', user_table);


app.mount('#frameapp');
