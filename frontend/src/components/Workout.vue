<template>
<div class="gs-workout">
  <div class="gs-workout__title">
    Workout
  </div>
  <div class="container mt-4">
    <div class="row">
      <div class="col">
        <Exercise class="my-2" v-for="(exercise, index) in exercises"
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

  @at-root #{&}__title {
    padding: 1em;
    background: linear-gradient(#003366, #00499b);
    font-size: 1.5rem;
    font-weight: bold;
    text-transform: uppercase;
    color: #ffffff;
  }
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
