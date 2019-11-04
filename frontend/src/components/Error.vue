<template>
<div class="my-4 error-container">
  <div v-if="errors" class="row">
    <div v-for="error in errors" :key="error" class="col error">
      {{ error }}
    </div>
  </div>
</div>
</template>

<script>
import { mapState } from 'vuex';

export default {
  name: 'Error',

  computed: {
    ...mapState({ errors: state => state.errorHandler.errors }),
  },
};
</script>

<style scoped>
.error-container {
  min-width: 400px;
}
.error {
  width: 100%;
  font-size: 0.75rem;
  font-weight: bold;
  padding: 8px;
  color: #721c24;
  background-color: #f8d7da;
  margin-bottom: 4px;
  border-radius: .25rem;
}
</style>
