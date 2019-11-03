<template>
<div class="container">
  <div class="row justify-content-center">
    <div class="col-6">
      <ErrorStack/>
      <div class="card">
        <div class="card-header">
          {{ title }}
        </div>
        <div class="card-body">
          <form>
            <div class="form-group">
              <label for="idNickname">
                Nickname
              </label>
              <input type="text" class="form-control" id="idNickname">
            </div>
            <div class="form-group">
              <label for="idFirstName">
                First name
              </label>
              <input type="text" class="form-control" id="idFirstName">
            </div>
            <div class="form-group">
              <label for="idLastName">
                Last name
              </label>
              <input type="text" class="form-control" id="idLastName">
            </div>
            <div class="form-group">
              <label for="idEmail">
                Email address
              </label>
              <input type="email" class="form-control" id="idEmail">
            </div>
            <div class="form-group">
              <label for="idPassword">
                Password
              </label>
              <input type="password" class="form-control" id="idPassword">
            </div>
            <div class="form-group">
              <label for="idPasswordRepeat">
                Repeat password
              </label>
              <input type="password" class="form-control" id="idPasswordRepeat">
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import ErrorStack from '@/components/ErrorStack.vue';

export default {
  name: 'Registration',
  components: { ErrorStack },
  data() {
    return {
      title: 'Sign Up',
    };
  },
};
</script>

<style scoped>

</style>
