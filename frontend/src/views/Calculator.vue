<template>
<div class="d-flex justify-content-center my-4">
  <div class="accordion md-accordion" id="calcAccardion" role="tablist"
       aria-multiselectable="true">
    <Wilks :show="chosenItem === 'Wilks'"/>
    <OneRepMax :show="chosenItem === 'OneRepMax'"/>
    <BMR :show="chosenItem === 'BMR'"/>
  </div>
</div>
</template>

<script>
import Wilks from '@/components/calculators/Wilks.vue';
import OneRepMax from '@/components/calculators/OneRepMax.vue';
import BMR from '@/components/calculators/BMR.vue';

export default {
  name: 'Calculator',

  props: ['chosenItem'],

  components: {
    Wilks,
    OneRepMax,
    BMR,
  },
};
</script>

<style scoped>

</style>
