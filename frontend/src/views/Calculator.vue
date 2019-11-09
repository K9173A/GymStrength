<template>
<div class="d-flex justify-content-center my-4">
  <div class="accordion md-accordion" id="calcAccardion" role="tablist"
       aria-multiselectable="true">
    <Wilks :show="chosenItem === 'Wilks'"/>
    <OneRepMax :show="chosenItem === 'OneRepMax'"/>
  </div>
</div>
</template>

<script>
import Wilks from '@/components/calculators/Wilks.vue';
import OneRepMax from '@/components/calculators/OneRepMax.vue';

export default {
  name: 'Calculator',

  props: ['chosenItem'],

  components: {
    Wilks,
    OneRepMax,
  },
};
</script>

<style scoped>

</style>
