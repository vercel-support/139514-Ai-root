<template>
  <!-- TODO: render in a nicer way -->
  <div>{{ content }}</div>
</template>

<script lang="ts" setup>
defineProps({
  content: {
    type: String,
    required: true,
  },
})
</script>

<style scoped lang="scss">
.container {
  @media screen and (max-width: 1024px) {
    width: 100%;
  }

  width: 80%;
}

</style>
