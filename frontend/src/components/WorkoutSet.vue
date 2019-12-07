<template>
<div class="gs-workout-set">
  <span class="gs-workout-set__weight">
    {{ getExerciseSet(exerciseId, setId).weight }} kg
  </span>
  <span class="gs-workout-set__times">
    <font-awesome-icon icon="times" size="sm"/>
  </span>
  <span class="gs-workout-set__repetitions">
    {{ getExerciseSet(exerciseId, setId).repetitions }} reps
  </span>
  <button type="button" class="gs-workout-set__edit"
          data-toggle="modal" data-target="#modal-create-product">
    <font-awesome-icon icon="ellipsis-v" />
  </button>
</div>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  name: 'WorkoutSet',

  props: ['setId', 'exerciseId'],

  computed: {
    ...mapGetters(['getExerciseSet']),
  },
};
</script>

<style scoped lang="scss">
.gs-workout-set {
  margin: 8px 8px 0 8px;
  border: 1px solid #b0b3b5;
  border-radius: 4px;
  background: linear-gradient(#ffffff, #e7e7e7);
  color: #6c757d;
  text-transform: uppercase;
  font-weight: 600;
  box-shadow: 2px 2px 2px 0 rgba(0, 0, 0, 0.25);

  @at-root #{&}__weight {
    padding: 4px;
  }

  @at-root #{&}__times {
    padding: 4px;
  }

  @at-root #{&}__repetitions {
    padding: 4px;
  }

  @at-root #{&}__edit {
    padding: 4px;
    border: none;
    background: none;
    color: #0069d2;
    transition: 0.3s;
    &:hover {
      color: #007dec;
    }
    &:focus {
      outline: none;
    }
  }
}
</style>
