const state = {
  workout: {
    prev: null,
    next: null,
    curr: 1,
    total: 1,
    count: 0,
  },
};

const actions = {};

const mutations = {
  setPaginationElement(state, { paginationName, elementName, value }) {
    state[paginationName][elementName] = value;
  }
};

const getters = {};

export default {
  actions,
  mutations,
  state,
  getters,
};
