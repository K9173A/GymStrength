<template>
<div class="gs-workout-set">
  <div class="d-flex">
    <div class="gs-workout-input-group">
      <span id="idWeight">Weight:</span>
      <input type="text" maxlength="4" aria-describedby="idWeight"
             :value="data.weight">
    </div>
    <div class="gs-workout-input-group">
      <span id="idReps">Repetitions:</span>
      <input type="text" maxlength="4" aria-describedby="idReps"
             :value="data.repetitions">
    </div>
  </div>
</div>
</template>

<script>
export default {
  name: 'WorkoutSet',

  props: ['data'],
};
</script>

<style scoped lang="scss">
$color-text: #1c92d2;

.gs-workout-set {
  display: inline-block;
  padding: 4px 0 4px 4px;
  border-top-left-radius: 4px;
  border-bottom-left-radius: 4px;
  background-color: #ffffff;
  box-shadow: 2px 2px 2px 0 rgba(0, 0, 0, 0.5);
}

.gs-workout-input-group {
  display: flex;
  margin-right: 16px;

  span {
    padding: 0 4px 0 4px;
    display: flex;
    align-items: center;
    color: $color-text;
    font-weight: 800;
    font-size: 1.2rem;
  }

  input {
    width: 48px;
    padding: 0 4px 0 4px;
    box-shadow: none;
    background-color: #ebebeb;
    border: none;
    transition: 0.3s;
    color: $color-text;
    font-weight: 800;
    font-size: 1.2rem;
    text-align: center;
    &:focus {
      outline: none;
    }
  }
}
</style>
