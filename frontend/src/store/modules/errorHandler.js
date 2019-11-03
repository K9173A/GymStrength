const mutations = {
  /**
   * Sets new error.
   * @param state - Vuex state object.
   * @param error - response object.
   */
  setError(state, error) {
    state.errors = [];
    if (error.response) {
      if (error.response.status === 500) {
        state.errors.push('500 Internal server error.');
        return;
      }
      if (error.response.status === 404) {
        state.errors.push('404 Not found.');
        return;
      }
      Object.entries(error.response.data).forEach((data) => {
        const [title, messages] = data;
        if (messages instanceof Array) {
          for (let i = 0; i < messages.length; i += 1) {
            state.errors.push(`${title}: ${messages[i]}`);
          }
        } else {
          state.errors.push(`${title}: ${messages}`);
        }
      });
    } else if (error.request) {
      state.errors.push(error.message);
    } else {
      state.errors.push(error.message);
    }
  },

  clear(state) {
    if (state) {
      state.errors = [];
    }
  },
};

const state = {
  errors: [],
};

export default {
  mutations,
  state,
};
