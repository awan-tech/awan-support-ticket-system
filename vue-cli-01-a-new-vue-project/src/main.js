import { createApp } from 'vue';

import App from './App.vue';
import login from './components/login.vue'
import template from './components/template.vue'
import header from './components/header.vue'
import create_btn from './components/create_btn.vue'
import user_table from './components/user_table.vue'
const app = createApp(App);

app.component('header-page', header ) ;
app.component( 'login-page', login ) ;
app.component('template-page', template ) ;
app.component('create-btn', create_btn);
app.component('user-table', user_table);

app.mount('#frameapp');
