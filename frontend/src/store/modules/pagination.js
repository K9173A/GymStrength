const state = {
  workout: {
    prev: null,
    next: null,
    curr: 1,
    total: 1,
    count: 0,
  },
  databaseExercise: {
    prev: null,
    next: null,
    curr: 1,
    total: 1,
    count: 0,
  },
  workoutExercise: {
    prev: null,
    next: null,
    curr: 1,
    total: 1,
    count: 0,
  },
};

const mutations = {
  /**
   * Sets new value of the specified pagination element.
   * @param state - Vuex object which stores states.
   * @param paginationName - name of pagination object.
   * @param elementName - name of pagination element (key).
   * @param value - new value of pagination element (value).
   */
  setPaginationElement(state, { paginationName, elementName, value }) {
    state[paginationName][elementName] = value;
  },
};

export default {
  mutations,
  state,
};
