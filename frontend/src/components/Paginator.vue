<template>
<nav>
  <ul class="pagination">
    <li :class="{ disabled: !getPaginationElement(paginationName, 'prev') }" class="page-item">
      <a v-if="paginationName === 'workouts'" class="page-link" aria-label="Previous"
         @onclick="fetchWorkouts(1)">
        <span aria-hidden="true">&laquo;</span>
      </a>
      <a v-if="paginationName === 'databaseExercises'" class="page-link" aria-label="Previous"
         @onclick="fetchDatabaseExercises(1)">
        <span aria-hidden="true">&laquo;</span>
      </a>
      <a v-if="paginationName === 'workoutExercises'" class="page-link" aria-label="Previous"
         @onclick="fetchWorkoutExercises(1)">
        <span aria-hidden="true">&laquo;</span>
      </a>
    </li>
    <li v-if="getPaginationElement(paginationName, 'prev')" class="page-item"
        aria-current="page">
      <a v-if="paginationName === 'workout'" class="page-link" aria-label="Previous"
         @onclick="fetchWorkouts(getPaginationElement(paginationName, 'prev'))">
        {{ getPaginationElement(paginationName, 'prev') }}
      </a>
      <a v-if="paginationName === 'databaseExercises'" class="page-link" aria-label="Previous"
         @onclick="fetchDatabaseExercises(getPaginationElement(paginationName, 'prev'))">
        {{ getPaginationElement(paginationName, 'prev') }}
      </a>
      <a v-if="paginationName === 'workoutExercises'" class="page-link" aria-label="Previous"
         @onclick="fetchWorkoutExercises(getPaginationElement(paginationName, 'prev'))">
        {{ getPaginationElement(paginationName, 'prev') }}
      </a>
    </li>
    <li class="page-item active" aria-current="page">
      <span class="page-link">
        {{ getPaginationElement(paginationName, 'curr') }}
      </span>
      <span class="sr-only">(current)</span>
    </li>
    <li v-if="getPaginationElement(paginationName, 'next')" class="page-item">
      <a v-if="paginationName === 'workout'" class="page-link" aria-label="Next"
         @onclick="fetchWorkouts(getPaginationElement(paginationName, 'next'))">
        {{ getPaginationElement(paginationName, 'next') }}
      </a>
      <a v-if="paginationName === 'databaseExercises'" class="page-link" aria-label="Next"
         @onclick="fetchDatabaseExercises(getPaginationElement(paginationName, 'next'))">
        {{ getPaginationElement(paginationName, 'next') }}
      </a>
      <a v-if="paginationName === 'workoutExercises'" class="page-link" aria-label="Next"
         @onclick="fetchWorkoutExercises(getPaginationElement(paginationName, 'next'))">
        {{ getPaginationElement(paginationName, 'next') }}
      </a>
    </li>
    <li :class="{ disabled: !getPaginationElement(paginationName, 'next') }" class="page-item">
      <a v-if="paginationName === 'workout'" class="page-link" aria-label="Next"
         @onclick="fetchWorkouts(getPaginationElement(paginationName, 'next'))">
        <span aria-hidden="true">&raquo;</span>
      </a>
      <a v-if="paginationName === 'databaseExercises'" class="page-link" aria-label="Next"
         @onclick="fetchDatabaseExercises(getPaginationElement(paginationName, 'next'))">
        <span aria-hidden="true">&raquo;</span>
      </a>
      <a v-if="paginationName === 'workoutExercises'" class="page-link" aria-label="Next"
         @onclick="fetchWorkoutExercises(getPaginationElement(paginationName, 'next'))">
        <span aria-hidden="true">&raquo;</span>
      </a>
    </li>
  </ul>
</nav>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';

export default {
  name: 'Paginator',

  props: ['paginationName'],

  computed: {
    ...mapGetters(['getPaginationElement']),
  },

  methods: {
    ...mapActions([
      'fetchWorkouts',
      'fetchDatabaseExercises',
      'fetchWorkoutExercises',
    ]),
  },
};
</script>

<style scoped>

</style>
