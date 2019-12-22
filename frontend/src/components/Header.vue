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
        <DropdownMenu/>
      </li>
      <li class="nav-item">
        <router-link active-class="active" :to="{ name: 'about' }"
                     class="nav-link menu__item">
          About
        </router-link>
      </li>
    </ul>
    <div class="col-xs-3 btn-group">
      <router-link :to="{ name: 'index' }" class="header-btn btn-search">
        <font-awesome-icon icon="search"/>
      </router-link>
      <router-link :to="{ name: 'registration' }" class="header-btn btn-user">
        <font-awesome-icon icon="user"/>
      </router-link>
    </div>
  </div>
</nav>
</template>

<script>
import DropdownMenu from '@/components/DropdownMenu.vue';

export default {
  name: 'Header',

  components: { DropdownMenu },

  data() {
    return {
      isVisible: false,
    };
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
  padding: 4px 8px 4px 8px;
  width: 64px;
  text-align: center;
  vertical-align: middle;
  font-size: 1rem;
  font-weight: 600;
  text-decoration: none;
  user-select: none;
  color: #1d1d1d;
}

.btn-search {
  background-color: $main-color;
  transition: all .3s;
  &:hover {
    background-color: #ffffff;
  }
}

.btn-user {
  background-color: #00b036;
  transition: all .3s;
  &:hover {
    background-color: #00c739;
  }
}

.active {
  color: #ffdc0a;
}
</style>
