<template>
<div class="gs-table">
  <div class="gs-table__title">
    Workout
  </div>
  <table class="table table-bordered table-striped">
    <thead class="gs-table__head">
      <tr>
        <th scope="col">#</th>
        <th scope="col">Exercise</th>
        <th scope="col">Sets</th>
      </tr>
    </thead>
    <tbody class="gs-table__body">
      <tr>
        <td>1</td>
        <td>2</td>
        <td>
          <ClosableTag/>
          <ClosableTag/>
          <ClosableTag/>
        </td>
      </tr>
      <tr>
        <td>2</td>
        <td>2</td>
        <td>3</td>
      </tr>
      <tr>
        <td>3</td>
        <td>2</td>
        <td>3</td>
      </tr>
      <tr>
        <td>4</td>
        <td>2</td>
        <td>3</td>
      </tr>
    </tbody>
  </table>
  <button type="button" class="btn gs-table__btn">
    <font-awesome-icon icon="plus" size="lg" />
  </button>
</div>
</template>

<script>
import ClosableTag from '@/components/ClosableTag.vue';

export default {
  name: 'Workout',

  components: { ClosableTag },
};
</script>

<style scoped lang="scss">
.gs-table {
  width: 100%;
  margin-bottom: 0;
  box-shadow: 0 0 5px rgba(40, 40, 40, 0.25);

  @at-root #{&}__title {
    padding: 1em;
    background: linear-gradient(#1c92d2, #00a5ff);
    font-size: 1.5rem;
    font-weight: bold;
    text-transform: uppercase;
  }

  @at-root #{&}__head {
    font-size: 1.2rem;
  }

  @at-root #{&}__body {
    font-size: 1.1rem;
  }

  @at-root #{&}__btn {
    width: 100%;
    background-color: #f6f6f6;
    color: #02c316;
    border-radius: 0;
    border-top: 2px solid #f0f0f0;

    &:hover {
      background-color: #f0f0f0;
    }

    &:focus {
      background-color: #e1e1e1;
      border-top: 2px solid #f0f0f0;
      box-shadow: none;
    }
  }
}
</style>
