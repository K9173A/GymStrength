<template>
<div class="gs-exercise">
  <div class="gs-exercise-header d-flex">
    <div class="col-1 gs-exercise-header__number">
      # {{ exerciseId }}
    </div>
    <div class="col gs-exercise-header__name">
      {{ getDatabaseExerciseName(exerciseId) }}
    </div>
  </div>
  <img src="https://via.placeholder.com/256" alt="exercise">
  <div class="gs-exercise-body">
    {{ getDatabaseExerciseDescription(exerciseId) }}
  </div>
</div>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  name: 'DatabaseExercise',

  props: ['exerciseId'],

  computed: {
    ...mapGetters([
      'getDatabaseExerciseName',
      'getDatabaseExerciseDescription',
    ]),
  },
};
</script>

<style scoped>

</style>
