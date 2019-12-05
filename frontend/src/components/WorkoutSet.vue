<template>
<div class="gs-workout-set">
  <div class="d-flex">
    <div class="gs-workout-input-group">
      <span id="idWeight">Weight:</span>
      <input type="number" pattern="[\d]{1,4}" maxlength="4"
             aria-describedby="idWeight" @input="setWeight"
             :value="getExerciseSet(exerciseId, setId).weight">
    </div>
    <div class="gs-workout-input-group">
      <span id="idReps">Repetitions:</span>
      <input type="text" pattern="[\d]{1,3}" maxlength="3"
             aria-describedby="idReps" @input="setRepetitions"
             :value="getExerciseSet(exerciseId, setId).repetitions">
    </div>
  </div>
</div>
</template>

<script>
import { mapMutations, mapGetters } from 'vuex';

export default {
  name: 'WorkoutSet',

  props: ['setId', 'exerciseId'],

  computed: {
    ...mapGetters(['getExerciseSet']),
  },

  methods: {
    ...mapMutations(['setWorkoutSetWeight', 'setWorkoutSetReps']),

    setWeight(event) {
      let newWeight = parseInt(event.target.value, 10);
      // Upper limit is equal to 999 kgs.
      if (newWeight < 1) {
        newWeight = 1;
      }
      // Upper limit is equal to 999 kgs.
      if (newWeight > 999) {
        newWeight = 999;
      }

      this.setWorkoutSetWeight({
        exerciseId: this.exerciseId,
        setId: this.setId,
        weight: newWeight,
      });
    },

    setRepetitions(event) {
      let newReps = parseInt(event.target.value, 10);
      if (newReps < 1) {
        newReps = 1;
      }
      this.setWorkoutSetReps({
        exerciseId: this.exerciseId,
        setId: this.setId,
        repetitions: newReps,
      });
    },
  },
};
</script>

<style scoped lang="scss">
.gs-workout-set {
  display: inline-block;
  padding: 4px 0 4px 4px;
  border: 1px solid lightgray;
  border-right: none;
  border-top-left-radius: 4px;
  border-bottom-left-radius: 4px;
  background: linear-gradient(#ffffff, #e7e7e7);
  text-shadow: 0 -1px 0 rgba(0, 0, 0, 0.25);
  box-shadow: 2px 2px 2px 0 rgba(0, 0, 0, 0.5);
}

.gs-workout-input-group {
  display: flex;
  margin-right: 16px;

  span {
    padding: 0 4px 0 4px;
    display: flex;
    align-items: center;
    color: #6c757d;
    font-weight: 800;
    font-size: 0.9rem;
    text-transform: uppercase;
    text-shadow: 0 -1px 0 #ffffff;
  }

  input {
    width: 48px;
    padding: 0 4px 0 4px;
    background: linear-gradient(#c5c4c4, #dcdcdc);
    transition: 0.3s;
    color: #007bff;
    font-weight: 800;
    font-size: 1.2rem;
    text-align: center;
    &:focus {
      outline: none;
    }
  }
}
</style>
