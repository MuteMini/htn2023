<script setup lang="ts">
import CameraWrapper from "./components/CameraWrapper.vue";
import { ref } from "vue";

const gestureOn = ref(false);
</script>

<template>
  <main class="d-flex flex-0-1 flex-column justify-center align-center">
    <CameraWrapper />
    <v-btn block rounded="lg" class="mt-5" @click="gestureOn = !gestureOn">
      <p v-if="gestureOn">Turn Off Gesture Control</p>
      <p v-else>Turn On Gesture Control</p>
    </v-btn>
  </main>
</template>

<style>
/* Hiding scrollbar from https://www.w3schools.com/howto/howto_css_hide_scrollbars.asp */

/* Hide scrollbar for Chrome, Safari and Opera */
::-webkit-scrollbar {
  display: none;
}

/* Hide scrollbar for IE, Edge and Firefox */
:root {
  -ms-overflow-style: none;
  scrollbar-width: none;

  font-synthesis: none;
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  -webkit-text-size-adjust: 100%;

  max-width: 1280px;
  margin: 0 auto;
  padding: 2rem;
  text-align: center;
}
</style>
