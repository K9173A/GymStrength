const state = {
  errors: [],
};

const mutations = {
  /**
   * Sets new error.
   * @param state - Vuex object which stores states.
   * @param error - response object.
   */
  setError(state, error) {
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
  /**
   * Removes error from the list.
   * @param state - Vuex object which stores states.
   * @param index - error index in the array.
   */
  removeError(state, index) {
    state.errors.splice(index, 1);
  },
  /**
   * Removes all errors from the list.
   * @param state - Vuex object which stores states.
   */
  clear(state) {
    state.errors = [];
  },
};

const getters = {
  /**
   * Gets list of errors.
   * @param state - Vuex object which stores states.
   * @returns {Array} list of errors.
   */
  getErrors: state => state.errors,
};

export default {
  mutations,
  state,
  getters,
};
