<template>
<div class="container my-4">
  <div class="row">
    <div class="col mx-4">
      <div class="nav nav-tabs" id="nav-tab" role="tablist">
        <a class="nav-item nav-link active" role="tab" data-toggle="tab" href="#nav-routines"
           id="nav-routines-tab" aria-controls="nav-routines" aria-selected="true">
          Routines
        </a>
        <a class="nav-item nav-link" role="tab" data-toggle="tab" href="#nav-metrics"
           id="nav-metrics-tab" aria-controls="nav-metrics" aria-selected="false">
          Metrics
        </a>
        <a class="nav-item nav-link" role="tab" data-toggle="tab" href="#nav-records"
           id="nav-records-tab" aria-controls="nav-records" aria-selected="false">
          Records
        </a>
      </div>
      <div class="tab-content m-2">
        <div class="tab-pane fade show active" role="tabpanel"
             id="nav-routines" aria-labelledby="nav-routines-tab">
          <Workout/>
        </div>
        <div class="tab-pane fade" role="tabpanel"
             id="nav-metrics" aria-labelledby="nav-metrics-tab">
          Metrics graphics
        </div>
        <div class="tab-pane fade" role="tabpanel"
             id="nav-records" aria-labelledby="nav-records-tab">
          My personal records
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import { mapActions } from 'vuex';
import Workout from '@/components/Workout.vue';

export default {
  name: 'Plan',

  components: { Workout },

  methods: {
    ...mapActions(['fetchWorkouts']),
  },

  mounted() {
    // this.fetchWorkouts();
  },
};
</script>

<style scoped>

</style>
