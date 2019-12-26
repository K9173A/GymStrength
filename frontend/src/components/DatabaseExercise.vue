<template>
<div class="gs-exercise">
  <div class="gs-exercise__header">
    {{ getDatabaseExerciseName(exerciseId) }}
  </div>
  <div class="gs-exercise__body">
    <img :src="getDatabaseExerciseImage(exerciseId)" alt="exercise">
    <p class="gs-exercise__text">
      {{ getDatabaseExerciseDescription(exerciseId) }}
    </p>
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
      'getDatabaseExerciseImage',
    ]),
  },
};
</script>

<style scoped lang="scss">
.gs-exercise {
  max-height: 290px;
  display: inline-block;
  overflow: hidden;
  border-radius: 8px;

  @at-root #{&}__header {
    padding: 0 16px 0 16px;
    font-size: 1.5rem;
    font-weight: 800;
    background-color: #4e4e4e;
  }

  @at-root #{&}__body {
    display: flex;
    background-color: #6e6e6e;
  }

  @at-root #{&}__text {
    padding: 16px;
    font-size: 1.3rem;
    font-weight: bold;
    text-align: justify;
  }
}
</style>
