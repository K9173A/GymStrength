<template>
<div class="d-flex justify-content-center my-4">
  <div class="accordion md-accordion" id="accordionEx" role="tablist"
       aria-multiselectable="true">
    <Wilks/>
  </div>
</div>
</template>

<script>
import Wilks from '@/components/calculators/Wilks.vue';

export default {
  name: 'Calculator',

  components: { Wilks },
};
</script>

<style scoped>

</style>
