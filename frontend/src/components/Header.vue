<template>
<nav class="navbar navbar-expand-lg p-3">
  <router-link :to="{ name: 'index' }" class="navbar-brand">
    <h5>LOGO</h5>
  </router-link>
  <ul class="nav navbar-nav mx-auto">
    <li>
      <router-link :to="{ name: 'index' }"
        class="nav-link rounded font-weight-bold text-center mx-2">
        Main
      </router-link>
    </li>
  </ul>
</nav>
</template>

<script>
export default {
  name: 'Header',
};
</script>

<style scoped>

</style>
