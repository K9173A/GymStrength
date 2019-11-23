<template>
<div class="gs-workout-set-box">
  <div class="gs-workout-set-box__header">
    <span>
      System:
    </span>
    <select>
      <option value="kg" selected>
        KG
      </option>
      <option value="lb">
        LB
      </option>
    </select>
  </div>
  <div class="gs-workout-set-box__body">
    <div class="container">
    <div class="row">
      <div class="col">
        <div class="gs-workout-set-wrapper" v-for="(set, index) in sets" :key="index">
          <WorkoutSet :data="set"/>
          <button @click="remove" class="gs-close-btn">
            <font-awesome-icon icon="times"/>
          </button>
        </div>
      </div>
    </div>
  </div>
  </div>
  <div class="gs-workout-set-box__footer">
    Total:
  </div>
</div>
</template>

<script>
import WorkoutSet from '@/components/WorkoutSet.vue';

export default {
  name: 'WorkoutSetBox',

  components: { WorkoutSet },

  props: ['sets'],

  methods: {
    remove() {
      console.log('remove item...');
    },
  },
};
</script>

<style scoped lang="scss">
.gs-workout-set-box {
  display: inline-block;
  margin: 16px;
  overflow: hidden;
  border-radius: 8px;
  background-color: #c6c8ca;
  box-shadow: 4px 4px 4px 0 rgba(0, 0, 0, 0.25);

  @at-root #{&}__header {
    padding: 8px;
    background-color: #606060;
  }

  @at-root #{&}__footer {
    padding: 8px;
    background-color: #606060;
  }
}

.gs-workout-set-wrapper {
  display: flex;
  margin: 8px;
}

.gs-close-btn {
  padding: 4px;
  background-color: #ffffff;
  border: none;
  border-top-right-radius: 4px;
  border-bottom-right-radius: 4px;
  color: #b30005;
  box-shadow: 2px 2px 2px 0 rgba(0, 0, 0, 0.5);
  transition: 0.3s;
  &:hover {
    color: #f20005;
  }
  &:focus {
    outline: none;
  }
}
</style>
