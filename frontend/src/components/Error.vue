<template>
<div v-if="getErrors" class="container">
  <div class="row">
    <div class="col">
      <div v-for="(error, index) in getErrors" :key="error" class="error">
        <span class="error__text">
          {{ error }}
        </span>
        <button type="button" @click="removeError(index)" class="error__btn">
          <font-awesome-icon icon="times" size="lg"/>
        </button>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import { mapGetters, mapMutations } from 'vuex';

export default {
  name: 'Error',

  computed: {
    ...mapGetters(['getErrors']),
  },

  methods: {
    ...mapMutations(['removeError']),
  },
};
</script>

<style scoped lang="scss">
.error {
  display: flex;
  justify-content: space-between;
  width: 100%;
  margin-bottom: 4px;
  padding: 16px;
  border-radius: 8px;
  background-color: #ca0b1f;

  @at-root #{&}__text {
    font-size: 1.25rem;
    font-weight: 700;
    color: #ececec;
  }

  @at-root #{&}__btn {
    padding: 4px;
    border: none;
    background: none;
    color: #ececec;
    transition: 0.3s;
    &:hover {
      color: #ffffff;
    }
    &:focus {
      outline: none;
    }
  }
}
</style>
