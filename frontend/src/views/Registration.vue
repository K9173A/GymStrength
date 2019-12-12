<template>
<div class="container">
  <div class="row justify-content-center">
    <div class="col-6">
      <div class="card form">
        <div class="card-body">
          <form id="register-form">
            <div class="form-group">
              <label for="idUsername" class="font-weight-bold">
                Username
              </label>
              <input type="text" class="form-control" id="idUsername" v-model="username">
            </div>
            <div class="form-group">
              <label for="idFirstName" class="font-weight-bold optional">
                First name
              </label>
              <input type="text" class="form-control" id="idFirstName" v-model="firstName">
            </div>
            <div class="form-group">
              <label for="idLastName" class="font-weight-bold optional">
                Last name
              </label>
              <input type="text" class="form-control" id="idLastName" v-model="lastName">
            </div>
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
            <div class="form-group">
              <label for="idPasswordRepeat" class="font-weight-bold">
                Repeat password
              </label>
              <input type="password" class="form-control" id="idPasswordRepeat" v-model="password2">
            </div>
          </form>
          <p class="text-secondary">
            By clicking "Sign up", you agree to our
            <a href="#">terms of service</a>,
            <a href="#">privacy policy</a> and
            <a href="#">cookie policy</a>
          </p>
          <div class="d-flex justify-content-around p-2">
            <button @click="$router.push({ name: 'index' })" class="btn btn-primary col-5">
              Cancel
            </button>
            <input type="submit" class="btn btn-primary col-5" form="register-form" value="Sign Up">
          </div>
          <hr>
          <p class="text-secondary">
            Already have an account?
            <a href="#">Log In</a>
          </p>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  name: 'Registration',

  data() {
    return {
      username: '',
      firstName: '',
      lastName: '',
      email: '',
      password: '',
      password2: '',
    };
  },

  methods: {
    ...mapActions(['register']),

    submit() {
      this.register({
        username: this.username,
        firstName: this.firstName,
        lastName: this.lastName,
        email: this.email,
        password: this.password,
      });
    },
  },
};
</script>

<style scoped>
.form {
  max-width: 30rem;
}

.optional::after {
  content: '*';
  color: red;
}
</style>
