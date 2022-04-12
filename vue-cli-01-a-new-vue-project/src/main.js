import { createApp } from 'vue';

import App from './App.vue';
import login from './components/login.vue'


const app = createApp(App);

app.component( 'login-page', login )

app.mount('#frameapp');
