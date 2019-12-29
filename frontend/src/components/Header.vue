<template>
<nav class="navbar navbar-expand-lg shadow-sm menu">
  <div class="container">
    <router-link :to="{ name: 'index' }" class="col-xs-3 navbar-brand menu__logo">
      <font-awesome-icon icon="dumbbell" size="lg"/>
      GYMSTRENGTH
    </router-link>
    <ul class="col-xs-6 navbar-nav mx-auto">
      <li class="nav-item">
        <router-link active-class="active" :to="{ name: 'index' }"
                     class="nav-link menu__item" exact>
          Main
        </router-link>
      </li>
      <li class="nav-item">
        <router-link active-class="active" :to="{ name: 'workouts', params: { page: 1 }}"
                     class="nav-link menu__item">
          Training plan
        </router-link>
      </li>
      <li class="nav-item">
        <router-link active-class="active" :to="{ name: 'databaseExercises', params: { page: 1 }}"
                     class="nav-link menu__item">
          Exercises
        </router-link>
      </li>
      <li class="nav-item">
        <router-link active-class="active" :to="{ name: 'about' }"
                     class="nav-link menu__item">
          About
        </router-link>
      </li>
    </ul>
    <ul class="col-xs-3 navbar-nav mx-auto">
      <router-link :to="{ name: 'login' }" class="header-btn mx-1">
        Log in
      </router-link>
      <router-link :to="{ name: 'registration' }" class="header-btn mx-1">
        Sign up
      </router-link>
    </ul>
  </div>
</nav>
</template>

<script>
export default {
  name: 'Header',

  data() {
    return { isVisible: false };
  },
};
</script>

<style scoped lang="scss">
$main-color: #ececec;

.menu {
  padding: 8px 0 8px 0;

  @at-root #{&}__item {
    font-size: 1.1rem;
    font-weight: 700;
    text-transform: uppercase;
    color: $main-color;
    border-top: 2px solid rgba(0, 0, 0, 0);
    border-bottom: 2px solid rgba(0, 0, 0, 0);
    transition: .3s ease-in-out;
    &:hover {
      border-top: 2px solid $main-color;
      border-bottom: 2px solid $main-color;
    }
  }
  @at-root #{&}__logo {
    text-align: center;
    color: $main-color;
    font-weight: 300;
    font-size: 1.7rem;
    text-transform: uppercase;
    letter-spacing: 6px;
  }
}

.header-btn {
  height: 100%;
  padding: 8px;
  min-width: 64px;
  text-align: center;
  vertical-align: middle;
  font-size: 0.9rem;
  font-weight: 600;
  text-decoration: none;
  text-transform: uppercase;
  border: 1px solid $main-color;
  color: $main-color;
  user-select: none;
  transition: all .3s;

  &:hover {
    border: 1px solid #ffdc0a;
    color: #ffdc0a;
  }
}

.active {
  color: #ffdc0a;
}
</style>
