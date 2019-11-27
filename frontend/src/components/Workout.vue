<template>
<div class="gs-workout">
  <div class="gs-workout-header d-flex align-items-center">
    <a href="#" class="gs-workout-calendar">
      <div class="gs-workout-month">
        Nov
      </div>
      <div class="gs-workout-day">
        30
      </div>
      <div class="gs-workout-weekday">
        Sat
      </div>
    </a>
    <span class="gs-workout-title">
      Workout
    </span>
  </div>
  <div class="container">
    <div class="row">
      <div class="col">
        <Exercise class="my-3" @clicked="deleted" v-for="(exercise, index) in exercises"
                  :key="exercise.name" :exercise="exercise" :index="index"/>
        <button type="button" class="my-2 btn gs-add-btn" @click="addExercise">
          Add Exercise
        </button>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import Exercise from '@/components/Exercise.vue';

export default {
  name: 'Workout',

  components: { Exercise },

  data() {
    return {
      exercises: [
        {
          name: 'MyExercise',
          sets: [
            {
              weight: 20,
              weightSystem: 'Metric',
              repetitions: 10,
            },
            {
              weight: 20,
              weightSystem: 'Metric',
              repetitions: 10,
            },
            {
              weight: 20,
              weightSystem: 'Metric',
              repetitions: 10,
            },
          ],
        },
      ],
    };
  },

  methods: {
    addExercise() {
      console.log('add row');
    },
    deleted(value) {
      console.log('Hello Wodl', value);
    },
  },
};
</script>

<style scoped lang="scss">
.gs-workout {
  width: 100%;
  overflow: hidden;
  box-shadow: 0 0 5px rgba(40, 40, 40, 0.25);
  border-radius: 16px;
  border: 1px solid #b3b3b3;
}

.gs-workout-header {
  padding: 16px;
  background: linear-gradient(180deg, #d6d8db, #e9ecef);
  border-bottom: 1px solid #b3b3b3;
}

.gs-workout-title {
  font-size: 3rem;
  font-weight: 800;
  letter-spacing: 5px;
  text-transform: uppercase;
  color: #6c757d;
}

.gs-workout-calendar {
  overflow: hidden;
  display: inline-block;
  margin-right: 32px;
  border: 1px solid #c2c2c2;
  border-radius: 5px;
  background: linear-gradient(#ffffff, #e7e7e7);
  letter-spacing: 2px;
  font-weight: 800;
  text-align: center;
  text-shadow: 0 -1px 0 rgba(0, 0, 0, 0.25);
  text-decoration: none;
}

.gs-workout-month {
  padding: 4px 8px 4px 8px;
  background: #a7a7a7;
  border-radius: 4px 4px 0 0;
  color: #ffffff;
  font-size: 0.8em;
  text-transform: uppercase;
  text-shadow: 0 -1px 0 rgba(0, 0, 0, 0.25);
}

.gs-workout-day {
  font-size: 1.3rem;
}

.gs-workout-weekday {
  font-size: 0.8rem;
}

.gs-add-btn {
  width: 100%;
  border-radius: 12px;
  border: 3px dashed #02a515;
  color: #02a515;
  font-size: 1.5rem;
  font-weight: 800;
  text-transform: uppercase;

  &:hover {
    border: 3px dashed #02c115;
    color: #02c115;
  }

  &:focus {
    box-shadow: none;
  }
}
</style>
