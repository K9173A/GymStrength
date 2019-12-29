import Vue from 'vue';

const state = {
  counter: 0,
  messages: {},
};

const actions = {
  /**
   * Adds new error message to the list.
   * @param state - Vuex object which stores states.
   * @param error - response object.
   */
  addErrorMessage({ commit }, error) {
    if (error.response) {
      if (error.response.status === 500) {
        commit('addMessage', {
          messageText: '500 Internal server error.',
          messageType: 'error',
        });
      } else if (error.response.status === 404) {
        commit('addMessage', {
          messageText: '404 Not found.',
          messageType: 'error',
        });
      } else if (error.response.status === 403) {
        commit('addMessage', {
          messageText: '403 Forbidden.',
          messageType: 'error',
        });
      } else {
        Object.entries(error.response.data).forEach((data) => {
          const [title, messages] = data;
          if (messages instanceof Array) {
            for (let i = 0; i < messages.length; i += 1) {
              commit('addMessage', {
                messageText: `${title}: ${messages[i]}`,
                messageType: 'error',
              });
            }
          } else {
            commit('addMessage', {
              messageText: error.message,
              messageType: 'error',
            });
          }
        });
      }
    } else {
      commit('addMessage', {
        messageText: error.message,
        messageType: 'error',
      });
    }
  },
};

const mutations = {
  /**
   * Adds message of specified type to the list.
   * @param state - Vuex object which stores states.
   * @param messageText - message text.
   * @param messageType - message type:
   * 'error' - errors and critical errors.
   * 'info' - debugging information and user notifications.
   * 'success' - successful completion of registration/activation/subscription.
   */
  addMessage(state, { messageText, messageType }) {
    Vue.set(state.messages, state.counter, { messageText, messageType });
    state.counter += 1;
  },
  /**
   * Removes message from the list.
   * @param state - Vuex object which stores states.
   * @param messageId - message id.
   */
  removeMessage(state, messageId) {
    Vue.delete(state.messages, messageId);
  },
  /**
   * Clears the list of errors.
   * @param state - Vuex object which stores states.
   */
  clear(state) {
    state.messages = {};
    state.counter = 0;
  },
};

const getters = {
  /**
   * Gets list of messages.
   * @param state - Vuex object which stores states.
   * @returns {Array} list of messages.
   */
  getMessages: state => state.messages,
};

export default {
  state,
  actions,
  mutations,
  getters,
};
