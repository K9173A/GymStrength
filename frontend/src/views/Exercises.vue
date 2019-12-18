<template>
  <div class="d-flex flex-column">
    <Exercise v-for="(id, index) in getExercisesIds" :key="id"
              :exerciseId="id" :exerciseIndex="index" class="my-3 mx-auto"/>
  </div>
</template>

<script>
import Exercise from '@/components/WorkoutExercise.vue';

export default {
  name: 'Exercises',

  components: { Exercise },
};
</script>

<style scoped>

</style>
