<template>
<div class="closable-tag">
  <div class="d-flex">
    <div class="set-data d-flex">
      <div class="set-data__item input-group input-group-sm">
    <div class="input-group-prepend">
      <span class="input-group-text" id="idWeight">
        W
      </span>
    </div>
    <input type="text" maxlength="4" class="form-control" aria-describedby="idWeight">
  </div>
      <div class="set-data__item d-flex align-items-center">
        <font-awesome-icon icon="times"/>
      </div>
      <div class="set-data__item input-group input-group-sm">
    <div class="input-group-prepend">
      <span class="input-group-text" id="idReps">
        R
      </span>
    </div>
    <input type="text" maxlength="4" class="form-control" aria-describedby="idReps">
  </div>
      <div class="set-data__item d-flex align-items-center">
        <font-awesome-icon icon="equals"/>
      </div>
      <div class="set-data__item input-group input-group-sm">
    <div class="input-group-prepend">
      <span class="input-group-text" id="idResult">
        T
      </span>
    </div>
    <input type="text" maxlength="10" class="form-control"
           aria-describedby="idResult" readonly>
  </div>
      <button @click="remove" class="close-btn set-data__item">
        <font-awesome-icon icon="times-circle"/>
      </button>
    </div>
  </div>
</div>
</template>

<script>
export default {
  name: 'ClosableTag',

  methods: {
    remove() {
      console.log('remove item...');
    },
  },
};
</script>

<style scoped lang="scss">
.closable-tag {
  display: inline-block;
  margin-bottom: 4px;
  padding: 4px 8px 4px 8px;
  border-radius: 4px;
  background-color: rgba(0, 180, 255, 0.28);
  box-shadow: 0 0 3px rgba(40, 40, 40, 0.25);
}

.close-btn {
  background-color: transparent;
  border: none;
  box-shadow: none;
  color: #f0f0f0;

  &:hover {
    color: #f6f6f6;
  }
}

.input-group {
  width: unset;
}

.form-control {
  width: 48px;
  flex: none;
  &:focus {
    box-shadow: none;
    border: 1px solid #ced4da;
  }
}

.set-data {
  color: #f0f0f0;

  @at-root #{&}__item {
    padding-right: 8px;
  }
}
</style>
