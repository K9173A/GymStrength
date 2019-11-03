<template>
<nav class="navbar navbar-expand-lg fixed-top shadow-sm menu">
  <div class="container">
    <router-link :to="{ name: 'index' }" class="col-xs-3 navbar-brand">
      <img src="@/assets/img/logo.png" class="menu__logo" alt="logo">
    </router-link>
    <ul class="col-xs-6 navbar-nav mx-auto">
      <li class="nav-item">
        <router-link :to="{ name: 'index' }" class="nav-link menu__item">
          Main
        </router-link>
      </li>
      <li class="nav-item">
        <router-link :to="{ name: 'plan' }" class="nav-link menu__item">
          Training plan
        </router-link>
      </li>
    </ul>
    <div class="col-xs-3 btn-group">
      <a href="#" class="btn btn-sign-up">
        Sign Up
      </a>
      <a href="#" class="btn btn-sign-in">
        Sign In
      </a>
    </div>
  </div>
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
  background-color: rgba(0, 78, 195, 0.68);

  @at-root #{&}__item {
    min-width: 64px;
    font-size: 1.25rem;
    font-weight: 800;
    text-transform: uppercase;
    color: #ffffff;
    transition: 0.4s ease-in-out;
    border-top: 4px solid rgba(0, 0, 0, 0);
    border-bottom: 4px solid rgba(0, 0, 0, 0);
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

.btn-sign-up {
  height: 32px;
  background-color: green;
  &:hover {
    background-color: yellowgreen;
  }
}
.btn-sign-in {
  height: 32px;
  background-color: yellowgreen;
}
</style>
