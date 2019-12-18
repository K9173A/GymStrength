import Vue from 'vue';
import Vuex from 'vuex';

import authentication from '@/store/modules/authentication';
import errorHandler from '@/store/modules/errorHandler';
import gym from '@/store/modules/gym';
import pagination from '@/store/modules/pagination';


Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    authentication,
    errorHandler,
    gym,
    pagination,
  },
});
