import Vue from 'vue';

import axios from 'axios';
import VueAxios from 'vue-axios';
import BootstrapVue from 'bootstrap-vue';

import 'bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import '@/assets/css/style.css';

import { library } from '@fortawesome/fontawesome-svg-core';
import {
  faUser, faSearch, faCaretDown, faPlus, faTimesCircle,
  faGripLinesVertical, faTimes, faCheck, faEllipsisV,
} from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

import App from './App.vue';
import store from './store';
import router from './router';


library.add(
  faUser, faSearch, faCaretDown, faPlus, faTimesCircle,
  faGripLinesVertical, faTimes, faCheck, faEllipsisV,
);

Vue.use(VueAxios, axios);
Vue.use(BootstrapVue);
Vue.component('font-awesome-icon', FontAwesomeIcon);

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app');
