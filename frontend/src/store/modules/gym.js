import Vue from 'vue';

const state = {
  workouts: null,
  workoutExercises: {
    1: {
      sets: {
        1: { weight: 80, repetitions: 5 },
        2: { weight: 80, repetitions: 5 },
        3: { weight: 80, repetitions: 5 },
        4: { weight: 80, repetitions: 5 },
        5: { weight: 80, repetitions: 5 },
      },
    },
  },
  databaseExercises: {
    1: {
      name: 'Bench press',
      description: 'This is bench press description!',
      image: null,
    }
  },
};

const actions = {
  /**
   * Fetches list of workouts.
   * @param dispatch - Vuex function which calls actions.
   * @param commit - Vuex function which calls mutations.
   * @param getters - Vuex object which stores getters.
   * @param id - user id.
   * @param page - requested page number.
   */
  fetchWorkouts({ dispatch, commit, getters }, { id, page }) {
    Vue.axios
      .get(`gym/list_workouts/user/${id}/?=${page}`, getters.getAuthHeaders())
      .then((response) => {
        dispatch('applyPagination', { response, paginationName: 'workout' });
        commit('setWorkouts', response.data.results);
      })
      .catch(error => commit('setError', error));
  },
  /**
   * Fetches list of database exercises.
   * @param dispatch - Vuex function which calls actions.
   * @param commit - Vuex function which calls mutations.
   * @param page - requested page number.
   */
  fetchDatabaseExercises({ dispatch, commit }, page) {
    Vue.axios
      .get(`gym/list_db_exercises/?=${page}`)
      .then((response) => {
        dispatch('applyPagination', { response, paginationName: 'databaseExercises' });
        commit('setDatabaseExercises');
      })
      .catch(error => commit('setError', error));
  },
  /**
   * Fetches list of workout exercises.
   * @param dispatch - Vuex function which calls actions.
   * @param commit - Vuex function which calls mutations.
   * @param id - user id.
   * @param page - requested page number.
   */
  fetchWorkoutExercises({ dispatch, commit }, { id, page }) {
    Vue.axios
      .get(`gym/list_exercises/user/${id}/?=${page}`, getters.getAuthHeaders())
      .then((response) => {
        dispatch('applyPagination', { response, paginationName: 'workoutExercises' });
        commit('setWorkoutExercises', response.data.results);
      })
      .catch(error => commit('setError', error));
  },
  /**
   * Sets new pagination information.
   * @param commit - Vuex function which calls mutations.
   * @param response - response object.
   * @param paginationName - name of pagination object.
   */
  applyPagination({ commit }, { response, paginationName }) {
    const elementNames = Object.keys(response.data);
    for (let i = 0; i < elementNames.length; i += 1) {
      const elementName = elementNames[i];
      if (elementName !== 'results') {
        commit('setPaginationElement', {
          paginationName, elementName, value: response.data[elementName],
        });
      }
    }
  },
};

const mutations = {
  /**
   * Sets list of exercises.
   * @param state - Vuex object which stores states.
   * @param exercises - exercises list.
   */
  setExercises(state, exercises) {
    state.exercises = exercises;
  },
  /**
   * Sets weight for the specified set of the specified exercise.
   * @param state - Vuex object which stores states.
   * @param exerciseId - exercise id.
   * @param setId - set id.
   * @param weight - new weight.
   */
  setWorkoutSetWeight(state, { exerciseId, setId, weight }) {
    state.exercises[exerciseId].sets[setId].weight = weight;
  },
  /**
   * Sets repetitions for the specified set of the specified exercise.
   * @param state - Vuex object which stores states.
   * @param exerciseId - exercise id.
   * @param setId - set id.
   * @param repetitions - new amount of repetitions.
   */
  setWorkoutSetReps(state, { exerciseId, setId, repetitions }) {
    state.exercises[exerciseId].sets[setId].repetitions = repetitions;
  },
};

const getters = {
  /**
   * Gets workout exercise name by its id.
   * @param state - Vuex object which stores states.
   * @returns {string} exercise name.
   */
  getWorkoutExerciseName: state => exerciseId => state.exercises[exerciseId].name,
  /**
   * Gets specific set of exercise.
   * @param state - Vuex object which stores states.
   * @returns {object} - set object.
   */
  getWorkoutExerciseSet: state => (exerciseId, setId) => state.exercises[exerciseId].sets[setId],
  /**
   * Gets object with all sets ids for the specified exercise.
   * @param state - Vuex object which stores states.
   * @returns {object} object which contains all sets ids for the specified
   * exercise.
   */
  getWorkoutExerciseSetsIds: state => exerciseId => Object.keys(state.exercises[exerciseId].sets),
  /**
   * Gets array of exercises ids which are being used
   * as keys in the exercises object.
   * @param state - Vuex object which stores states.
   * @returns {string[]} array of Ids.
   */
  getWorkoutExercisesIds: state => Object.keys(state.exercises),
  /**
   * Calculates total weight for the specified exercise.
   * @param state - Vuex object which stores states.
   * @returns {number} total weight for the specified exercise.
   */
  getWorkoutExerciseTotalWeight: state => (exerciseId) => {
    let totalWeight = 0;
    const exercise = state.exercises[exerciseId];
    const keys = Object.keys(exercise.sets);
    for (let i = 0; i < keys.length; i += 1) {
      const key = keys[i];
      totalWeight += exercise.sets[key].weight * exercise.sets[key].repetitions;
    }
    return totalWeight;
  },
  /**
   * Calculates total amount of repetitions for the specified exercise.
   * @param state - Vuex object which stores states.
   * @returns {number} total amount of repetitions for the specified exercise.
   */
  getWorkoutExerciseTotalReps: state => (exerciseId) => {
    let totalReps = 0;
    const exercise = state.exercises[exerciseId];
    const keys = Object.keys(exercise.sets);
    for (let i = 0; i < keys.length; i += 1) {
      const key = keys[i];
      totalReps += exercise.sets[key].repetitions;
    }
    return totalReps;
  },
  /**
   * Gets object with database exercises ids.
   * @param state - Vuex object which stores states.
   * @returns {object} object with exercises.
   */
  getDatabaseExercisesIds: state => Object.keys(state.databaseExercises),
  /**
   * Gets database exercise name.
   * @param state - Vuex object which stores states.
   * @returns {string} database exercise name.
   */
  getDatabaseExerciseName: state => exerciseId => state.databaseExercises[exerciseId].name,
  /**
   * Gets database exercise description.
   * @param state - Vuex object which stores states.
   * @returns {string} database exercise description.
   */
  getDatabaseExerciseDescription:
      state => exerciseId => state.databaseExercises[exerciseId].description,
};

export default {
  state,
  actions,
  mutations,
  getters,
};
