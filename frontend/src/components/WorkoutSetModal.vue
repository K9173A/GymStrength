<template>
<div class="modal fade" id="modal-create-product" tabindex="-1"
     role="dialog" aria-labelledby="label" aria-hidden="true">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="label">
          Edit workout set
        </h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        MODAL BODY
      </div>
      <div class="modal-footer d-flex justify-content-around">
        <button type="button" class="btn btn-secondary btn-default" data-dismiss="modal">
          Cancel
        </button>
        <button type="button" class="btn btn-secondary" id="add-button">
          Save
        </button>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import { mapMutations } from 'vuex';

export default {
  name: 'WorkoutSetModal',

  methods: {
    ...mapMutations(['setWorkoutSetWeight', 'setWorkoutSetReps']),

    setWeight(event) {
      // event.target.value.match(/[0-9]/)
      let newWeight = parseInt(event.target.value, 10);

      // console.log(newWeight);

      if (Number.isFinite(newWeight)) {
        if (newWeight < 1) {
          newWeight = 1;
        } else if (newWeight > 999) {
          newWeight = 999;
        }
      } else {
        newWeight = 1;
        event.target.value = 1; // eslint-disable-line no-param-reassign
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

<style scoped>

</style>
