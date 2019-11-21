<template>
<div class="gs-exercise">
  <div class="row no-gutters">
    <img src="https://place-hold.it/256x256">
    <div class="col">
      <div class="gs-exercise-header">
        <div class="gs-exercise-header__number">
          #{{ index + 1 }}
        </div>
        <div class="gs-exercise-header__name">
          {{ exercise.name }}
        </div>
      </div>
      <div class="card-body">
        <WorkoutSetBox :sets="exercise.sets"/>
        <div class="col">
          <button type="button" class="btn gs-del-btn">
            <font-awesome-icon icon="times" size="lg"/>
          </button>
        </div>
      </div>
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
.gs-exercise {
  overflow: hidden;
  border-radius: 8px;
  background-color: #2aabd2;
  box-shadow: 4px 4px 4px 0 rgba(0, 0, 0, 0.25);
}

.gs-exercise-header {
  -webkit-box-flex: 1;
  flex: 1 1 auto;
  font-size: 1.2rem;
  font-weight: 800;
  color: white;

  @at-root #{&}__number {
    padding: 8px;
    background-color: #f20005;
  }

  @at-root #{&}__name {
    padding: 8px;
    background-color: #606060;
  }
}
</style>
