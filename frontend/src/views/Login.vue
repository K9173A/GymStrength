<template>
<div class="gs-form container">
  <div class="row justify-content-center">
    <div class="col-5">
      <div class="card form">
        <div class="card-body">
          <form id="login-form">
            <div class="form-group">
              <label for="idEmail" class="font-weight-bold">
                Email address
              </label>
              <input type="email" class="form-control" id="idEmail" v-model="email">
            </div>
            <div class="form-group">
              <label for="idPassword" class="font-weight-bold">
                Password
              </label>
              <input type="password" class="form-control" id="idPassword" v-model="password">
            </div>
          </form>
          <div class="d-flex justify-content-around p-2">
            <button @click="$router.push({ name: 'index' })" class="form-btn col-5">
              Cancel
            </button>
            <input type="submit" class="form-btn col-5" form="login-form" value="Sign Up">
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script>
export default {
  name: 'Login',

  data() {
    return {
      email: '',
      password: '',
    };
  },
};
</script>

<style scoped>

</style>
