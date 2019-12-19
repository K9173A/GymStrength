<template>
<div class="gs-exercise">
  <div class="gs-exercise-header d-flex">
    <div class="col-1 gs-exercise-header__number">
      #{{ exerciseIndex + 1 }}
    </div>
    <div class="col-10 gs-exercise-header__name">
      {{ getWorkoutExerciseName(exerciseId) }}
    </div>
    <div class="col-1 gs-exercise-header__close">
      <button type="button" class="btn gs-del-btn">
        <font-awesome-icon icon="times" size="lg"/>
      </button>
    </div>
  </div>
  <img src="https://via.placeholder.com/256" alt="exercise">
  <div class="gs-exercise-body">
    <div class="gs-workout-set-list-scroller">
      <div class="d-flex flex-column">
        <WorkoutSet v-for="(id, index) in getWorkoutExerciseSetsIds(exerciseId)" :key="id"
          :setId="id" :setIndex="index" :exerciseId="exerciseId"/>
      </div>
    </div>
    <div class="gs-workout-set-total d-flex align-items-center justify-content-around">
      <div class="badge badge-primary">
        Weight | {{ getWorkoutExerciseTotalWeight(exerciseId) }} kg
      </div>
      <div class="badge badge-primary">
        Repetitions | {{ getWorkoutExerciseTotalReps(exerciseId) }}
      </div>
    </div>
  </div>
</div>
</template>

<script>
import { mapGetters } from 'vuex';
import WorkoutSet from '@/components/WorkoutSet.vue';

export default {
  name: 'WorkoutExercise',

  components: { WorkoutSet },

  props: ['exerciseId', 'exerciseIndex'],

  computed: {
    ...mapGetters([
      'getWorkoutExerciseName',
      'getWorkoutExerciseSetsIds',
      'getWorkoutExerciseTotalWeight',
      'getWorkoutExerciseTotalReps',
    ]),
  },
};
</script>

<style scoped lang="scss">
$header-color: #0069d2;

img {
  float: left;
}

.form-control {
  width: unset;
}

.gs-exercise {
  max-height: 290px;
  display: inline-block;
  overflow: hidden;
  border-radius: 8px;
  background-color: #e8ebee;
  box-shadow: 4px 4px 4px 0 rgba(0, 0, 0, 0.25);
}

.gs-exercise-header {
  font-size: 1.5rem;
  font-weight: 800;
  color: #ffffff;
  background-color: $header-color;

  @at-root #{&}__number {
    display: flex;
    justify-content: center;
    align-items: center;
    padding-right: 0;
  }

  @at-root #{&}__name {
    display: flex;
    align-items: center;
  }

  @at-root #{&}__close {
    display: flex;
    align-items: center;
    padding-left: 0;
  }
}

.gs-exercise-body {
  display: flex;
  flex-direction: column;
}

.gs-workout-set-list-scroller {
  display: inline-block;
  height: 224px;
  overflow-y: scroll;
}

.gs-workout-set-list {
  display: flex;
  flex-direction: column;
}

.gs-workout-set-total {
  height: 32px;
  padding: 4px 8px 4px 8px;
  border-top: 1px solid #b3b3b3;
  color: #6c757d;
  font-size: 1.2rem;
  text-transform: uppercase;
}

.gs-exercise-options {
  color: #ffffff;
  font-size: 1.2rem;
  font-weight: 800;
}

.gs-del-btn {
  color: #f20005;
  &:hover {
    color: #ff0005;
  }
  &:focus {
    outline: none;
    box-shadow: none;
  }
}

.gs-close-btn {
  padding: 4px;
  border: 1px solid lightgray;
  border-left: none;
  border-top-right-radius: 4px;
  border-bottom-right-radius: 4px;
  background: linear-gradient(#ffffff, #e7e7e7);
  color: #b30005;
  box-shadow: 2px 2px 2px 0 rgba(0, 0, 0, 0.5);
  transition: 0.3s;
  &:hover {
    color: #f20005;
  }
  &:focus {
    outline: none;
  }
}
</style>
