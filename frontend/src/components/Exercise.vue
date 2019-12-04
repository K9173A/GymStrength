<template>
<div class="gs-exercise">
  <div class="gs-exercise-header d-flex">
    <div class="col-1 gs-exercise-header__number">
      #{{ exerciseIndex + 1}}
    </div>
    <div class="col-9 gs-exercise-header__name">
      {{ getExerciseName(exerciseId) }}
    </div>
    <div class="col-1 gs-exercise-header__system">
      <select class="form-control form-control-sm"
              @change="onChangeUnits($event.target.value)">
        <option value="Metric" selected>KG</option>
        <option value="Imperial">LB</option>
      </select>
    </div>
    <div class="col-1 gs-exercise-header__close">
      <button type="button" class="btn gs-del-btn">
        <font-awesome-icon icon="times" size="lg"/>
      </button>
    </div>
  </div>
  <img src="https://via.placeholder.com/256" alt="exercise">
  <div class="gs-exercise-body">
    <div class="gs-workout-set-list">
      <div v-for="(id, index) in getExerciseSetsIds(exerciseId)" :key="id"
           class="gs-workout-set-wrapper">
        <WorkoutSet :setId="id" :setIndex="index" :exerciseId="exerciseId"/>
        <button class="gs-close-btn">
          <font-awesome-icon icon="times" size="lg"/>
        </button>
      </div>
    </div>
    <div class="gs-workout-set-total d-flex align-items-center justify-content-around">
      <div class="badge badge-primary">
        Total reps: {{ getExerciseTotalReps(exerciseId) }}
      </div>
      <div class="badge badge-primary">
        Total weight: {{ getExerciseTotalWeight(exerciseId) }}
      </div>
    </div>
  </div>
</div>
</template>

<script>
import { mapGetters, mapMutations } from 'vuex';
import WorkoutSet from '@/components/WorkoutSet.vue';

export default {
  name: 'Exercise',

  components: { WorkoutSet },

  props: ['exerciseId', 'exerciseIndex'],

  computed: {
    ...mapGetters([
      'getExerciseName',
      'getExerciseSetsIds',
      'getExerciseTotalWeight',
      'getExerciseTotalReps',
    ]),
  },

  methods: {
    ...mapMutations(['setExerciseWeightSystem']),

    onChangeUnits(weightSystem) {
      this.setExerciseWeightSystem({
        exerciseId: this.exerciseId,
        weightSystem,
      });
    },
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

  @at-root #{&}__system {
    display: flex;
    align-items: center;
  }

  @at-root #{&}__close {
    display: flex;
    align-items: center;
  }
}

.gs-exercise-body {
  display: flex;
  flex-direction: column;
}

.gs-workout-set-list {
  display: inline-block;
  height: 224px;
  overflow-y: scroll;
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

.gs-workout-set-wrapper {
  display: flex;
  margin: 8px;
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
