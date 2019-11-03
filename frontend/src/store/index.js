import Vue from 'vue';
import Vuex from 'vuex';

import authentication from '@/store/modules/authentication';
import errorHandler from '@/store/modules/errorHandler';

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    authentication,
    errorHandler,
  },
});
