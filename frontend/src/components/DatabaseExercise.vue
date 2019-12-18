<template>
<div class="gs-exercise">
  <div class="gs-exercise-header d-flex">
    <div class="col-1 gs-exercise-header__number">
      #{{ exerciseIndex + 1 }}
    </div>
    <div class="col-10 gs-exercise-header__name">
      {{ getExerciseName(exerciseId) }}
    </div>
    <div class="col-1 gs-exercise-header__close">
      <button type="button" class="btn gs-del-btn">
        <font-awesome-icon icon="times" size="lg"/>
      </button>
    </div>
  </div>
  <img src="https://via.placeholder.com/256" alt="exercise">
  <div class="gs-exercise-body">

  </div>
</div>
</template>

<script>
export default {
  name: 'DatabaseExercise',
};
</script>

<style scoped>

</style>
