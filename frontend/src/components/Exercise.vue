<template>
<div class="gs-exercise">
  <div class="gs-exercise-header row">
    <div class="col-1 gs-exercise-header__number">
      #{{ index + 1 }}
    </div>
    <div class="col-10 gs-exercise-header__name">
      {{ exercise.name }}
    </div>
    <div class="col-1 gs-exercise-header__close">
      <button type="button" class="btn gs-del-btn">
        <font-awesome-icon icon="times" size="lg"/>
      </button>
    </div>
  </div>
  <div class="row">
    <div class="gs-exercise-options col-4">
      <img src="https://via.placeholder.com/256" alt="exercise">
      <div class="container m-2">
        <div class="row">
          <span>System: </span>
          <select class="form-control form-control-sm">
            <option value="kg" selected>KG</option>
            <option value="lb">LB</option>
          </select>
        </div>
        <div class="row">
          <span>Total: {{ total }}</span>
        </div>
      </div>
    </div>
    <div class="gs-exercise-body col">
      <div class="container">
        <div class="row">
          <div class="col">
            <div v-for="(set, index) in exercise.sets" :key="index"
                 class="gs-workout-set-wrapper">
              <WorkoutSet :data="set"/>
              <button @click="remove" class="gs-close-btn">
                <font-awesome-icon icon="times" size="lg"/>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import WorkoutSet from '@/components/WorkoutSet.vue';

export default {
  name: 'Exercise',

  components: { WorkoutSet },

  props: ['index', 'exercise'],

  data() {
    return {
      total: 0,
    };
  },

  methods: {
    remove() {
      console.log('remove item...');
    },

    calculateTotal() {

    },
  },
};
</script>

<style scoped lang="scss">
$header-color: #a7a7a7;

.form-control {
  width: unset;
}

.gs-exercise {
  overflow: hidden;
  border-radius: 8px;
  background-color: #dddddd;
  box-shadow: 4px 4px 4px 0 rgba(0, 0, 0, 0.25);
}

.gs-exercise-header {
  font-size: 1.5rem;
  font-weight: 800;
  color: white;

  @at-root #{&}__number {
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: #0007f2;
    padding-right: 0;
  }

  @at-root #{&}__name {
    display: flex;
    align-items: center;
    background-color: $header-color;
  }

  @at-root #{&}__close {
    display: flex;
    align-items: center;
    background-color: $header-color;
  }
}

.gs-exercise-options {
  background-color: $header-color;
  color: red;
  font-size: 1.2rem;
  font-weight: 800;
}

.gs-workout-set-wrapper {
  display: flex;
  margin: 8px;
}

.gs-del-btn {
  color: #f20005;
  &:hover {
    color: #ff0005;
  }
  &:focus {
    outline: none;
    box-shadow: none;
  }
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
