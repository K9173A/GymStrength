<template>
<div class="dropdown menu__item">
  <router-link class="nav-link nav-link--main" :to="{ name: 'calculators' }">
    Calculators <font-awesome-icon icon="caret-down" size="sm" />
  </router-link>
  <div class="dropdown__content">
    <a href="#" class="nav-link" v-for="item in items" :key="item" @click="onClick(item)">
      {{ item }}
    </a>
  </div>

</div>
</template>

<script>
export default {
  name: 'DropdownMenu',

  data() {
    return {
      items: [
        'Wilks',
        'OneRepMax',
      ],
    };
  },

  methods: {
    toggle() {
      this.show = !this.show;
    },

    onClick(item) {
      if (this.$router.currentRoute.name === 'calculators') {
        switch (item) {
          case 'Wilks':
            document.getElementById('wilksCollapse').classList.add('show');
            break;
          case 'OneRepMax':
            document.getElementById('ormCollapse').classList.add('show');
            break;
          default:
            throw Error('Invalid item value!');
        }
      } else {
        this.$router.push({ name: 'calculators', params: { chosenItem: item } });
      }
    },
  },
};
</script>

<style scoped lang="scss">
.nav-link--main {
  color: #ffffff;
}

.dropdown {
  &:hover #{&}__content {
    visibility: visible;
    opacity: 1;
  }
  #{&}__content {
    width: 100%;
    visibility: hidden;
    opacity: 0;
    z-index: 1;
    position: absolute;
    transition: opacity 0.3s linear;
    background-color: #ffffff;
    border: 2px solid #afafaf;
    padding: 6px;
    font-size: 1rem;
    text-transform: none;
  }
}
</style>
