<template>
  <div id="app">
    <div class="layout-wrapper">
      <Header/>
      <router-view/>
    </div>
    <Footer/>
  </div>
</template>

<script>
import Header from '@/components/Header.vue';
import Footer from '@/components/Footer.vue';

export default {
  components: {
    Header,
    Footer,
  },
};
</script>

<style lang="scss">
#app {
  display: flex;
  flex-direction: column;
  height: 100%;
}
</style>
