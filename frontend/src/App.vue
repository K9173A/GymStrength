<template>
  <div id="app">
    <div class="layout-wrapper">
      <Header/>
      <MessageList/>
      <router-view/>
    </div>
    <Footer/>
  </div>
</template>

<script>
import Header from '@/components/Header.vue';
import Footer from '@/components/Footer.vue';
import MessageList from '@/components/MessageList.vue';

export default {
  components: {
    MessageList,
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
