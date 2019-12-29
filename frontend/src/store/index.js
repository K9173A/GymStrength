import Vue from 'vue';
import Vuex from 'vuex';

import authentication from '@/store/modules/authentication';
import message from '@/store/modules/message';
import gym from '@/store/modules/gym';
import pagination from '@/store/modules/pagination';


Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    authentication,
    message,
    gym,
    pagination,
  },
});
