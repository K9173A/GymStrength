<template>
<div class="container">
  <div class="mx-auto">
    <div class="activation-box">
      <p class="activation-box__text">Activation success!</p>
      <router-link :to="{ name: 'index' }" class="activation-box__btn">
        На главную
      </router-link>
    </div>
  </div>
</div>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  name: 'Activation',

  props: ['uid', 'token'],

  methods: {
    ...mapActions(['activate']),
  },

  mounted() {
    this.activate({
      uid: this.$props.uid,
      token: this.$props.token,
    });
  },
};
</script>

<style scoped lang="scss">
.activation-box {
  display: flex;
  justify-content: space-between;
  padding: 16px;
  font-size: 1.5rem;
  font-weight: 700;
  border-radius: 8px;
  background-color: #00b036;

  @at-root #{&}__text {
    margin: unset;
  }

  @at-root #{&}__btn {
    height: 100%;
    padding: 4px 8px 4px 8px;
    text-align: center;
    vertical-align: middle;
    font-size: 1.2rem;
    font-weight: 700;
    text-decoration: none;
    user-select: none;
    border-radius: 5px;
    color: #1d1d1d;
    background-color: #ececec;
    transition: all .3s;
    &:hover {
      background-color: #ffffff;
    }
  }
}
</style>
