<template>
<div class="gs-exercise">
  <img src="https://via.placeholder.com/256" alt="exercise">
    <div class="gs-exercise-content">
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
      <div class="gs-exercise-body">
        <WorkoutSetBox :sets="exercise.sets"/>
      </div>
    </div>
</div>
</template>

<script>
import WorkoutSetBox from '@/components/WorkoutSetBox.vue';

export default {
  name: 'Exercise',

  components: { WorkoutSetBox },

  props: ['index', 'exercise'],
};
</script>

<style scoped lang="scss">
img {
  float: left;
}

.gs-exercise {
  overflow: hidden;
  border-radius: 8px;
  background-color: #dddddd;
  box-shadow: 4px 4px 4px 0 rgba(0, 0, 0, 0.25);
}

.gs-exercise-header {
  font-size: 1.2rem;
  font-weight: 800;
  color: white;

  @at-root #{&}__number {
    display: flex;
    align-items: center;
    background-color: #f20005;
    text-align: center;
  }

  @at-root #{&}__name {
    display: flex;
    align-items: center;
    background-color: #606060;
  }

  @at-root #{&}__close {
    display: flex;
    align-items: center;
    background-color: #606060;
  }
}

.gs-del-btn {
  color: #f20005;

  &:focus {
    outline: none;
  }
}
</style>
