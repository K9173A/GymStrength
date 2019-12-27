import Vue from 'vue';
import router from '../../router';


const state = {
  accessTokenKey: 'jwtAccessToken',
  refreshTokenKey: 'jwtRefreshToken',
};

const actions = {
  /**
   * Validates JWT access token.
   * @param commit - Vuex function which calls mutations.
   * @param getters - Vuex object which stores getters.
   */
  verifyToken({ commit, getters }) {
    Vue.axios
      .post('auth/jwt/verify', { token: getters.getAccessToken() })
      .catch(error => commit('setError', error));
  },
  /**
   * Refreshes JWT access token using JWT refresh token.
   * @param commit - Vuex function which calls mutations.
   * @param getters - Vuex object which stores getters.
   */
  refreshToken({ commit, getters }) {
    Vue.axios
      .post('auth/jwt/refresh', { refresh: getters.getRefreshToken() })
      .then((response) => {
        commit('setAccessToken', response.data.access);
        commit('setRefreshToken', response.data.refresh);
      })
      .catch(error => commit('setError', error));
  },
  /**
   * Logs user in by acquiring pair of JWT tokens.
   * @param commit - Vuex function which calls mutations.
   * @param credentials - object with username and password fields.
   */
  login({ commit }, credentials) {
    Vue.axios
      .post('auth/jwt/create/', credentials)
      .then((response) => {
        commit('setAccessToken', response.data.access);
        commit('setRefreshToken', response.data.refresh);
        router.push({ name: 'index' });
      })
      .catch(error => commit('setError', error));
  },
  /**
   * Logs user out by clearing his auth token.
   * @param commit - Vuex function which calls mutations.
   */
  logout({ commit }) {
    commit('removeAccessToken');
  },
  /**
   * Registers user.
   * @param commit - Vuex function which calls mutations.
   * @param credentials - object with the following fields:
   * username, firstName, lastName, email, password.
   */
  register({ commit }, credentials) {
    return Vue.axios
      .post('auth/users/', credentials)
      .then(() => true)
      .catch(error => commit('setError', error));
  },
  /**
   * Sends uid and token to confirm user account activation.
   * @param commit - Vuex function which calls mutations.
   * @param credentials - user's uid and token.
   */
  activate({ commit }, credentials) {
    Vue.axios
      .post('auth/users/activation/', credentials)
      .then(() => router.push({ name: 'index' }))
      .catch(error => commit('setError', error));
  },
};

const mutations = {
  /**
   * Writes access token to the localStorage.
   * @param state - Vuex object which stores states.
   * @param accessToken - access token.
   */
  setAccessToken(state, accessToken) {
    localStorage.setItem(state.accessTokenKey, accessToken);
  },
  /**
   * Writes refresh token to the localStorage.
   * @param state - Vuex object which stores states.
   * @param refreshToken - refresh token.
   */
  setRefreshToken(state, refreshToken) {
    localStorage.setItem(state.refreshTokenKey, refreshToken);
  },
  /**
   * Removes access token.
   * @param state - Vuex object which stores states.
   */
  removeAccessToken(state) {
    localStorage.removeItem(state.accessTokenKey);
  },
};

const getters = {
  /**
   * Gets access token from the local storage.
   * @param state - Vuex object which stores states.
   * @returns {string} access token.
   */
  getAccessToken(state) {
    return localStorage.getItem(state.accessTokenKey);
  },
  /**
   * Gets refresh token from the local storage.
   * @param state - Vuex object which stores states.
   * @returns {string} refresh token.
   */
  getRefreshToken(state) {
    return localStorage.getItem(state.refreshTokenKey);
  },
  /**
   * Gets authentication headers with JWT token.
   * @param state - Vuex object which stores states.
   * @returns {object} object with headers.
   */
  getAuthHeaders(state) {
    return {
      headers: {
        Authorization: `Bearer ${localStorage.getItem(state.accessTokenKey)}`,
      },
    };
  },
};

export default {
  state,
  actions,
  mutations,
  getters,
};
