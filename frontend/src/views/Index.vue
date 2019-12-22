<template>
<div class="masthead">
  <div class="d-flex justify-content-center">
    <div class="my-auto">
      <div class="my-2 masthead__title">
        Want to be strong?
      </div>
      <div class="my-2 masthead__text">
        GymStrength - your way of planning gym workouts
      </div>
      <div class="d-flex justify-content-center">
        <router-link :to="{ name: 'registration' }" class="my-4 masthead__btn">
          Get started
        </router-link>
      </div>
    </div>
    <img src="../assets/img/kk.png" alt="kk">
  </div>
</div>
</template>

<script>
export default {
  name: 'Index',
};
</script>

<style scoped lang="scss">
$main-color: #ececec;

.masthead {
  padding: 32px;
  min-height: 800px;
  color: $main-color;

  @at-root #{&}__title {
    font-size: 2.5rem;
    font-weight: 600;
    text-align: center;
    letter-spacing: 7px;
    text-transform: uppercase;
  }

  @at-root #{&}__text {
    font-size: 1.2rem;
    text-align: center;
    letter-spacing: 3px;
    text-transform: uppercase;
  }

  @at-root #{&}__btn {
    padding: 16px 64px 16px 64px;
    text-align: center;
    vertical-align: middle;
    font-size: 1.5rem;
    font-weight: 600;
    text-decoration: none;
    border: 3px solid $main-color;
    color: $main-color;
    user-select: none;
    transition: all .3s;
    &:hover {
      border: 3px solid #ffdc0a;
      color: #ffdc0a;
    }
  }
}

img {
  width: 500px;
}
</style>
