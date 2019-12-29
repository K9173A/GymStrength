<template>
<div class="gs-form container">
  <div class="row justify-content-center">
    <div class="col-5">
      <div class="card form">
        <div class="card-body">
          <form id="login-form">
            <div class="form-group">
              <label for="idUsername" class="font-weight-bold">
                Username
              </label>
              <input type="text" class="form-control" id="idUsername" v-model="username">
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
            <input type="submit" @click="submit" class="form-btn col-5" form="login-form"
                   value="Sign Up">
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  name: 'Login',

  data() {
    return {
      username: '',
      password: '',
    };
  },

  methods: {
    ...mapActions(['login', 'addErrorMessage']),

    submit() {
      this.login({
        username: this.username,
        password: this.password,
      }).then(() => {
        this.$router.push({ name: 'index' }).catch(error => this.addErrorMessage(error));
      });
    },
  },
};
</script>

<style scoped>

</style>
