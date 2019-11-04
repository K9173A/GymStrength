import Vue from 'vue';

import axios from 'axios';
import VueAxios from 'vue-axios';
import BootstrapVue from 'bootstrap-vue';

import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import '@/assets/css/style.css';

import { library } from '@fortawesome/fontawesome-svg-core';
import { faUser, faSearch, faCaretDown } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

import App from './App.vue';
import router from './router';
import store from './store';


library.add(faUser);
library.add(faSearch);
library.add(faCaretDown);

Vue.use(VueAxios, axios);
Vue.use(BootstrapVue);
Vue.component('font-awesome-icon', FontAwesomeIcon);

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app');
