<template>
  <q-page class="column items-center justify-evenly splash" padding>
    <router-link to="/chat">
      <q-img
      src="src/pages/view.png"
      class="q-mr-sm"
      width="70px"
      height="70px"
      alt="My Icon"
    />
    </router-link>
  </q-page>
</template>
<script lang="ts" setup>
</script>

<style scoped lang="scss">
.q-card {
  @media screen and (max-width: 1024px) {
    width: 100%;
  }

  width: 50%;

  .q-input {
    margin: 0.5rem;
  }
}

.splash {
  background-color: gray;
}

.header {
  display: flex;
  flex-direction: column;
  align-items: center;
  color: white;

  .title {
    font-size: 2rem;
    font-weight: bold;
  }

  .description {
    font-size: 1rem;
  }
}

.goal {
  display: flex;
  align-items: center;

  .q-input {
    width: 100%;
  }

  .q-icon {
    margin: 0.25rem;
    cursor: pointer;
  }
}
.q-btn {
    color: rgb(255, 255, 255);
    background: rgb(26, 44, 60);

    }
.q-btn.text-primary{
  color: rgb(255, 255, 255) !important;
}
.q-card__actions .q-btn--rectangle {
    padding: 0 15px;
}

</style>
