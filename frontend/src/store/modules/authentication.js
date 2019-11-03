import token from '@/scripts/token';

const actions = {
  /**
   * Logs user out by clearing his auth token.
   * @param context - context object.
   */
  logout(context) {
    context.commit('clearAuthenticationTokens');
    context.commit('setAuthenticated', false);
  },
};

const mutations = {
  setAuthenticated(state, isAuthenticated) {
    state.isAuthenticated = isAuthenticated;
  },
  /**
   * Sets user authentication data including a token.
   * @param state - Vuex state object.
   * @param response - response object.
   */
  setAuthenticationTokens(state, response) {
    token.save(token.accessTokenKey, response.data.access);
    token.save(token.refreshTokenKey, response.data.refresh);
  },
  /**
   * Clears user authentication data.
   */
  clearAuthenticationTokens() {
    token.delete(token.accessTokenKey);
  },
};

const state = {
  isAuthenticated: false,
};

export default {
  actions,
  mutations,
  state,
};
