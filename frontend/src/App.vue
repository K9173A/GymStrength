<template>
  <div id="app">
    <div class="layout-wrapper">
      <Header/>
      <Error/>
      <router-view/>
    </div>
    <Footer/>
  </div>
</template>

<script>
import Header from '@/components/Header.vue';
import Footer from '@/components/Footer.vue';
import Error from '@/components/Error.vue';

export default {
  components: {
    Error,
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
