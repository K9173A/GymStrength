<template>
<nav class="navbar navbar-expand-lg shadow-sm menu">
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
      <li class="nav-item">
        <div class="dropdown">
          <button type="button" @click="isVisible = !isVisible">
            Calculators<font-awesome-icon icon="caret-down" size="lg" />
          </button>
          <div :class="{'invisible': !isVisible}">
            <h3 style="color: red">HELLO WORLD</h3>
          </div>
        </div>
      </li>
    </ul>
    <div class="col-xs-3 btn-group">
      <a href="#" class="btn btn-search">
        <font-awesome-icon icon="search" size="lg" />
      </a>
      <router-link :to="{ name: 'registration' }" class="btn btn-user">
        <font-awesome-icon icon="user" size="lg" />
      </router-link>
    </div>
  </div>
</nav>
</template>

<script>
export default {
  name: 'Header',

  data() {
    return {
      isVisible: false,
    };
  },
};
</script>

<style scoped lang="scss">
.menu {
  padding-top: 16px;
  padding-bottom: 16px;
  background: linear-gradient(#003366, #00499b);

  @at-root #{&}__item {
    min-width: 64px;
    font-size: 1.2rem;
    font-weight: 700;
    text-transform: uppercase;
    color: #ffffff;
    transition: 0.4s ease-in-out;
    border-top: 2px solid rgba(0, 0, 0, 0);
    border-bottom: 2px solid rgba(0, 0, 0, 0);
    &:hover {
      border-top: 2px solid #ffffff;
      border-bottom: 2px solid #ffffff;
    }
  }
  @at-root #{&}__logo {
    width: 32px;
    height: 32px;
  }
}

.btn {
  border-radius: 0.5em;
}

.btn-search,
.btn-user {
  height: 100%;
  width: 64px;
  border: none;
}

.btn-search {
  color: #0076eb;
  background-color: #cdcdcd;
  &:hover {
    background-color: #ebebeb;
  }
}
.btn-user {
  color: #ffffff;
  background-color: #0069d2;
  &:hover {
    background-color: #0076eb;
  }
}

.invisible {
  display: none;
  opacity: 0;
}

</style>
