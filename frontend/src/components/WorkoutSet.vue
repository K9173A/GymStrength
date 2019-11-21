<template>
<div class="workout-set">
  <div class="d-flex">
    <div class="workout-set-content d-flex">
      <div class="workout-input-group">
        <span id="idWeight">W</span>
        <input type="text" maxlength="4" aria-describedby="idWeight"
               :value="data.weight">
      </div>
      <div class="workout-input-group">
        <span id="idReps">R</span>
        <input type="text" maxlength="4" aria-describedby="idReps"
               :value="data.repetitions">
      </div>
      <button @click="remove" class="close-btn">
        <font-awesome-icon icon="times"/>
      </button>
    </div>
  </div>
</div>
</template>

<script>
export default {
  name: 'ClosableTag',

  props: ['data'],

  methods: {
    remove() {
      console.log('remove item...');
    },
  },
};
</script>

<style scoped lang="scss">
.workout-set {
  display: inline-block;
  margin: 4px;
  padding: 4px;
  border-radius: 4px;
  background: linear-gradient(#1c92d2, #00a5ff);
  box-shadow: 0 0 3px rgba(40, 40, 40, 0.25);
}

.close-btn {
  background: none;
  border: none;
  box-shadow: none;
  color: #f20005;
  &:hover {
    color: #f6f6f6;
  }
  &:focus {
    outline: none;
    color: #ffffff;
  }
}

.workout-set-content {
  color: #f0f0f0;
  > div {
    margin-right: 4px;
  }
}

.workout-input-group {
  display: flex;

  span {
    padding: 0 4px 0 4px;
    display: flex;
    align-items: center;
    border-bottom: 3px solid #ffffff;
    background-color: #ffffff;
    color: #1c92d2;
    font-weight: 800;
    font-size: 1.1rem;
  }

  input {
    width: 48px;
    padding: 0 4px 0 4px;
    box-shadow: none;
    background: none;
    border: none;
    border-bottom: 3px solid #ffffff;
    transition: 0.3s;
    color: #ffffff;
    font-weight: 800;
    font-size: 1.1rem;

    &:focus {
      outline: none;
    }
  }
}
</style>
