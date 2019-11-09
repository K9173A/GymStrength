<template>
<div class="content-wrapper">
  <div class="masthead">
    <div class="container">
      <div class="row">
        <div class="col-7 masthead__content">
          <div class="masthead__title text-uppercase">
            What is GymStrength?
          </div>
          <div class="masthead__text text-justify">
            For every sportsman and healthy lifestyle enthusiast, who trains in a gym, creation and
            maintenance of training plan is important part of his/her progress. If particular
            training system or complex is being composed incorrectly, most likely it will eventually
            cause so-called "plate state" - when you stuck and can't progress anymore. In some cases
            it can even cause regression in weights. This is where you need GymStrength! So what is
            exactly GymStrength? It's a software/service which helps to compose and maintain
            training plan. Furthermore, it has embedded analysis modules which are very useful for
            tracking own progress.
          </div>
        </div>
      </div>
      <div class="row mt-4 justify-content-center">
        <a href="#" class="btn btn-primary">
          Try now!
        </a>
      </div>
    </div>
  </div>
</div>
</template>

<script>
export default {
  name: 'Index',
};
</script>

<style scoped lang="scss">
.content-wrapper {
  margin-top: 0;
}

.container {
  margin-left: 96px;
}

.masthead {
  min-height: 800px;
  background: url("../assets/img/barbell.jpg") no-repeat;
  background-size: cover;
  color: #ffffff;

  @at-root #{&}__content {
    margin-top: 96px;
    padding: 32px;
    border-radius: 5%;
    background-color: rgba(0, 78, 195, 0.68);
  }

  @at-root #{&}__title {
    font-size: 2.75rem;
    text-align: center;
    font-weight: bold;
    letter-spacing: 3px;
  }

  @at-root #{&}__text {
    font-size: 1.5rem;
    text-align: justify;
  }
}
</style>
