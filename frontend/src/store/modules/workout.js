const state = {
  exercises: {
    1: {
      name: 'Bench press',
      sets: {
        1: { weight: 80, repetitions: 5 },
        2: { weight: 80, repetitions: 5 },
        3: { weight: 80, repetitions: 5 },
        4: { weight: 80, repetitions: 5 },
        5: { weight: 80, repetitions: 5 },
      },
    },
  },
};

const actions = {
  /**
   * Fetches a chunk of workouts.
   * @param commit - Vuex function which calls mutations.
   * @param state - Vuex object which stores states.
   * @param getters - Vuex object which stores getters.
   * @param id - user id.
   * @param page - current page number.
   */
  fetchWorkouts({ commit, state, getters }, { id, page }) {
    Vue.axios
      .get(`gym/list_workouts/user/${id}/?=${page}`, getters.getAuthHeaders())
      .then((response) => {
        const keys = Object.keys(response.data);
        for (let i = 0; i < keys.length; i += 1) {
          const key = keys[i];
          if (key === 'results') {
            continue;
          }
          commit('setPaginationElement', {
            paginationName: 'workout',
            elementName: key,
            value: response.data[key],
          });
        }
        commit('setExercises', response.data.results);
      })
      .catch(error => commit('setError', error));
  },

  createWorkout() {
    Vue.axios
      .post(`gym/create_workout/`, {

      }, token.getAuthHeaders())
  },

  addExercise() {

    // show modal window
    // axios add!
    console.log('show modal form');
  },

  deleteExercise(exerciseId) {
    // axios delete!
    console.log(exerciseId);
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
   * Gets exercise name by its id.
   * @param state - Vuex object which stores states.
   * @returns {string} exercise name.
   */
  getExerciseName: state => exerciseId => state.exercises[exerciseId].name,
  /**
   * Gets specific set of exercise.
   * @param state - Vuex object which stores states.
   * @returns {object} - set object.
   */
  getExerciseSet: state => (exerciseId, setId) => state.exercises[exerciseId].sets[setId],
  /**
   * Gets object with all sets ids for the specified exercise.
   * @param state - Vuex object which stores states.
   * @returns {object} object which contains all sets ids for the specified
   * exercise.
   */
  getExerciseSetsIds: state => exerciseId => Object.keys(state.exercises[exerciseId].sets),
  /**
   * Gets array of exercises ids which are being used
   * as keys in the exercises object.
   * @param state - Vuex object which stores states.
   * @returns {string[]} array of Ids.
   */
  getExercisesIds: state => Object.keys(state.exercises),
  /**
   * Calculates total weight for the specified exercise.
   * @param state - Vuex object which stores states.
   * @returns {number} total weight for the specified exercise.
   */
  getExerciseTotalWeight: state => (exerciseId) => {
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
   * @param state - Vuex object which stores states..
   * @returns {number} total amount of repetitions for the specified exercise.
   */
  getExerciseTotalReps: state => (exerciseId) => {
    let totalReps = 0;
    const exercise = state.exercises[exerciseId];
    const keys = Object.keys(exercise.sets);
    for (let i = 0; i < keys.length; i += 1) {
      const key = keys[i];
      totalReps += exercise.sets[key].repetitions;
    }
    return totalReps;
  },
};

export default {
  state,
  actions,
  mutations,
  getters,
};
