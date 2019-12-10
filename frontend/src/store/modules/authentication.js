const state = {
  accessTokenKey: 'jwtAccessToken',
  refreshTokenKey: 'jwtRefreshToken',
};

const actions = {
  /**
   * Logs user out by clearing his auth token.
   * @param context - context object.
   */
  logout({ commit }) {
    commit('removeAccessToken');
  },
  /**
   * Validates JWT access token.
   * @param getters - Vuex object which stores getters.
   */
  verifyToken({ getters }) {
    Vue.axios
      .post('auth/jwt/verify', { token: getters.getAccessToken() })
      .then(() => true)
      .catch(() => false);
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
        return true;
      })
      .catch(() => false);
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
        Authorization: `Bearer ${localStorage.getItem(state.accessTokenKey)}`
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
