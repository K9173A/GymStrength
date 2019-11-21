<template>
<div class="gs-workout">
  <div class="gs-workout__title">
    Workout
  </div>
  <div class="container mt-4">
    <div class="row">
      <div class="col">
        <div v-for="(exercise, index) in exercises" :key="exercise.name">
          <Exercise :exercise="exercise" :index="index"/>
          <button type="button" class="btn gs-del-btn">
            <font-awesome-icon icon="times" size="lg"/>
          </button>
        </div>
        <button type="button" class="btn gs-add-btn" @click="addExercise">
          <font-awesome-icon icon="plus" size="lg"/>
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
  box-shadow: 0 0 5px rgba(40, 40, 40, 0.25);

  @at-root #{&}__title {
    padding: 1em;
    background: linear-gradient(#1c92d2, #00a5ff);
    font-size: 1.5rem;
    font-weight: bold;
    text-transform: uppercase;
  }
}

.gs-add-btn {
  width: 100%;
  background-color: #f6f6f6;
  color: #02c316;
  border-radius: 0;
  border-top: 2px solid #f0f0f0;

  &:hover {
    background-color: #f0f0f0;
  }

  &:focus {
    background-color: #e1e1e1;
    border-top: 2px solid #f0f0f0;
    box-shadow: none;
  }
}

.gs-del-btn {
  width: 100%;
  color: #f20005;

  &:focus {
    outline: none;
  }
}
</style>
