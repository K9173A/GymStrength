<template>
<div class="container my-4">
  <Paginator :paginationName="'databaseExercises'" />
  <div class="d-flex flex-column">
    <DatabaseExercise v-for="(id, index) in getDatabaseExercisesIds" :key="id"
              :exerciseId="id" :exerciseIndex="index" class="my-3 mx-auto"/>
  </div>
</div>
</template>

<script>
import { mapGetters } from 'vuex';
import DatabaseExercise from '@/components/DatabaseExercise.vue';
import Paginator from '@/components/Paginator.vue';

export default {
  name: 'ExercisesList',

  components: { DatabaseExercise, Paginator },

  computed: {
    ...mapGetters(['getDatabaseExercisesIds']),
  },
};
</script>

<style scoped>

</style>
