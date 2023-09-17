<script setup lang="ts">
import Camera from "./Camera.vue";
import { ref } from "vue";

const cameraConnecting = ref(false);
const showCamera = ref(false);

function load() {
  cameraConnecting.value = true;
  showCamera.value = true;
}

function onConnect(id: string) {
  if (id == "error") showCamera.value = false;
  cameraConnecting.value = false;
}
</script>

<template>
  <v-card color="primary-darken-1" class="py-4" width="500">
    <v-btn
      v-if="!showCamera"
      :loading="cameraConnecting"
      class="flex-grow-1"
      height="48"
      variant="tonal"
      @click="load"
    >
      Connect Your Camera
    </v-btn>
    <Camera v-if="showCamera" @connect="onConnect" />
  </v-card>
</template>
