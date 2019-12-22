<template>
<div class="gs-workout">
  <div class="gs-workout-header d-flex align-items-center">
    <a href="#" class="gs-workout-calendar">
      <div class="gs-workout-month">Nov</div>
      <div class="gs-workout-day">30</div>
      <div class="gs-workout-weekday">Sat</div>
    </a>
    <span class="gs-workout-title">
      Workout
    </span>
  </div>
  <div class="d-flex flex-column">
    <Exercise v-for="(id, index) in getExercisesIds" :key="id"
              :exerciseId="id" :exerciseIndex="index" class="my-3 mx-auto"/>
    <button type="button" class="m-2 btn gs-add-btn">
      Add Exercise
    </button>
  </div>
  <WorkoutSetModal/>
</div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
import Exercise from '@/components/WorkoutExercise.vue';
import WorkoutSetModal from '@/components/WorkoutSetModal.vue';

export default {
  name: 'Workout',

  components: { Exercise, WorkoutSetModal },

  computed: {
    ...mapGetters(['getExercisesIds']),
  },

  methods: {
    ...mapActions(['fetchWorkouts']),
  },

  created() {
    this.fetchWorkouts({ id: 1, page: 1 });
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
  font-size: 0.8rem;
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
