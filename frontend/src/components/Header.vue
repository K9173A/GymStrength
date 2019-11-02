<template>
<nav class="navbar navbar-expand-lg p-3 menu">
  <router-link :to="{ name: 'index' }" class="navbar-brand">
    <img src="@/assets/img/logo.png" class="menu__logo" alt="logo">
  </router-link>
  <ul class="nav navbar-nav mx-auto">
    <li>
      <router-link :to="{ name: 'index' }" class="nav-link text-uppercase mx-2 menu__item">
        Main
      </router-link>
    </li>
    <li>
      <router-link :to="{ name: 'plan' }" class="nav-link text-uppercase mx-2 menu__item">
        Training plan
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

<style scoped lang="scss">
.menu {
  padding-top: 16px;
  padding-bottom: 16px;
  background-color: #2c61c3;

  @at-root #{&}__item {
    min-width: 64px;
    font-size: 1.25rem;
    font-weight: 800;
    color: #ffffff;
    transition: 0.4s ease-in-out;
    background: #2c61c3;
    border-top: 4px solid #2c61c3;
    border-bottom: 4px solid #2c61c3;
    &:hover {
      border-top: 4px solid #ffffff;
      border-bottom: 4px solid #ffffff;
    }
  }
  @at-root #{&}__item--active {
    color: green;
  }
  @at-root #{&}__logo {
    width: 32px;
    height: 32px;
  }
}
</style>
