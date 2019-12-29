<template>
<div class="container">
  <div class="row">
    <div class="col">
      <div v-for="(message, id) in getMessages" :key="id"
           class="message-box" :class="message.messageType">
        <span class="message-box__text">
          {{ message.messageText }}
        </span>
        <button type="button" @click="removeMessage(id)" class="message-box__btn">
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
  name: 'MessageList',

  computed: {
    ...mapGetters(['getMessages']),
  },

  methods: {
    ...mapMutations(['removeMessage']),
  },
};
</script>

<style scoped lang="scss">
.message-box {
  display: flex;
  justify-content: space-between;
  width: 100%;
  margin-bottom: 4px;
  padding: 8px;
  border-radius: 4px;

  @at-root #{&}__text {
    display: flex;
    align-items: center;
    font-size: 1rem;
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

.error {
  background-color: #ff0b1f;
}

.info {
  background-color: #6f6f6f;
}

.success {
  background-color: #00c739;
}
</style>
