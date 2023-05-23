<template>
  <q-layout view="lHh Lpr lFf">
    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script lang="ts" setup></script>

<style scoped lang="scss">
.q-page-container {
    background: rgb(255, 255, 255);
    // background: url(background.png) repeat fixed rgb(21, 35, 47);
    overflow-y: auto;
}


</style>
