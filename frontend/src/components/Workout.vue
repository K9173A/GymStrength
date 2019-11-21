<template>
<div class="gs-table">
  <div class="gs-table__title">
    Workout
  </div>
  <table class="table table-bordered table-striped">
    <thead class="gs-table__head">
      <tr>
        <th scope="col">#</th>
        <th scope="col">Exercise</th>
        <th scope="col">Sets</th>
        <th scope="col">Action</th>
      </tr>
    </thead>
    <tbody class="gs-table__body">
      <tr v-for="(exercise, index) in exercises" :key="exercise.name">
        <td>{{ index + 1 }}</td>
        <td>{{ exercise.name }}</td>
        <td>
          <ClosableTag v-for="(set, index) in exercise.sets" :key="index" :data="set"/>
        </td>
        <td>
          <button type="button" class="btn gs-del-btn">
            <font-awesome-icon icon="times" size="lg"/>
          </button>
        </td>
      </tr>
    </tbody>
  </table>
  <button type="button" class="btn gs-add-btn" @click="addExercise">
    <font-awesome-icon icon="plus" size="lg"/>
  </button>
</div>
</template>

<script>
import ClosableTag from '@/components/WorkoutSet.vue';

export default {
  name: 'Workout',

  components: { ClosableTag },

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
.table {
  margin-bottom: 0;
}

.gs-table {
  width: 100%;
  box-shadow: 0 0 5px rgba(40, 40, 40, 0.25);

  @at-root #{&}__title {
    padding: 1em;
    background: linear-gradient(#1c92d2, #00a5ff);
    font-size: 1.5rem;
    font-weight: bold;
    text-transform: uppercase;
  }

  @at-root #{&}__head {
    font-size: 1.2rem;
  }

  @at-root #{&}__body {
    font-size: 1.1rem;
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
