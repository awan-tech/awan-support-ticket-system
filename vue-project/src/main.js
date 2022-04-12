import { createApp } from 'vue';

import App from './App.vue';
import login from './components/login.vue'
import template from './components/template.vue'
import header from './components/header.vue'


const app = createApp(App);

app.component('header-page', header ) ;
app.component( 'login-page', login ) ;
app.component('template-page', template ) ;


app.mount('#frameapp');
