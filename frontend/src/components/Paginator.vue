<template>
<nav>
  <ul class="pagination">
    <li :class="{ disabled: !getPaginationElement(paginationName, 'prev') }" class="page-item">
      <router-link class="page-link" aria-label="Previous"
                   :to="{ name: paginationName, params: { page: 1 }}">
        <span aria-hidden="true">&laquo;</span>
      </router-link>
    </li>
    <li v-if="getPaginationElement(paginationName, 'prev')" class="page-item" aria-current="page">
      <router-link class="page-link" aria-label="Previous"
                   :to="{ name: paginationName, params: {
                     page: getPaginationElement(paginationName, 'prev') }}">
        {{ getPaginationElement(paginationName, 'prev') }}
      </router-link>
    </li>
    <li class="page-item active" aria-current="page">
      <span class="page-link">
        {{ getPaginationElement(paginationName, 'curr') }}
      </span>
      <span class="sr-only">(current)</span>
    </li>
    <li v-if="getPaginationElement(paginationName, 'next')" class="page-item">
      <router-link class="page-link" aria-label="Next"
                   :to="{ name: paginationName, params: {
                     page: getPaginationElement(paginationName, 'next') }}">
        {{ getPaginationElement(paginationName, 'next') }}
      </router-link>
    </li>
    <li :class="{ disabled: !getPaginationElement(paginationName, 'next') }" class="page-item">
      <router-link class="page-link" aria-label="Next"
                   :to="{ name: paginationName, params: {
                     page: getPaginationElement(paginationName, 'next') }}">
        <span aria-hidden="true">&raquo;</span>
      </router-link>
    </li>
  </ul>
</nav>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';

export default {
  name: 'Paginator',

  props: ['paginationName'],

  computed: {
    ...mapGetters(['getPaginationElement']),
  },

  methods: {
    ...mapActions([
      'fetchWorkouts',
      'fetchDatabaseExercises',
      'fetchWorkoutExercises',
    ]),
  },
};
</script>

<style scoped>

</style>
