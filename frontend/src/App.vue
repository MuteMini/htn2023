<script setup lang="ts">
import { ref, onMounted } from "vue";

const isCameraOpen = ref(false);
const cameraRef = ref<HTMLVideoElement | null>(null);

onMounted(() => {
  cameraRef.value?.focus();
});

const cameraConnecting = ref(false);
const showCamera = ref(false);
const gestureOn = ref(false);

const socket = ref<WebSocket>(new WebSocket("ws://127.0.0.1:3000"));
socket.value?.addEventListener("open", () => {});
socket.value?.addEventListener("error", () => {
  setTimeout(() => {
    socket.value = new WebSocket("ws://127.0.0.1:3000"); //Try reconnecting after 15 sec.
  }, 15000);
});

const canvas = document.createElement("canvas");
canvas.width = 620;
canvas.height = 400;
const ctx = canvas.getContext("2d");

function createCamera() {
  cameraConnecting.value = true;
  showCamera.value = true;
  const constraints = {
    audio: false,
    video: true,
  };
  navigator.mediaDevices
    .getUserMedia(constraints)
    .then((stream) => {
      if (cameraRef.value) {
        cameraRef.value.srcObject = stream;
        isCameraOpen.value = true;
      }
    })
    .catch((error) => {
      alert(`${error}: The browser could not find a camera.`);
      cameraConnecting.value = false;
      showCamera.value = false;
    });
}

function onGestureClick() {
  gestureOn.value = !gestureOn.value;

  if (gestureOn.value) {
    const message = setInterval(() => {
      if (!gestureOn.value) clearInterval(message);

      if (!socket.value) return;
      if (socket.value.readyState != 1) return;
      if (!ctx) return;
      if (!cameraRef.value) return;

      ctx.drawImage(cameraRef.value, 0, 0, canvas.width, canvas.height);
      const dataURI = canvas.toDataURL("image/jpeg");
      if (dataURI) socket.value?.send(dataURI);
    }, 50);
  }
}
</script>

<template>
  <main>
    <v-app class="d-flex flex-1-1 flex-column justify-center align-center">
      <v-card color="primary-darken-1" class="py-4" width="500">
        <v-btn
          v-if="!showCamera"
          :loading="cameraConnecting"
          class="flex-grow-1"
          height="48"
          variant="tonal"
          @click="createCamera"
        >
          Connect Your Camera
        </v-btn>
        <div v-if="showCamera" class="d-flex flex-row justify-center">
          <video
            v-show="isCameraOpen"
            class="ms-2 rounded"
            ref="cameraRef"
            :width="450"
            :height="337"
            autoplay
            playsinline
          ></video>
        </div>
      </v-card>
      <v-btn
        block
        rounded="lg"
        max-height="50px"
        class="mt-5"
        :color="gestureOn ? 'primary' : 'secondary'"
        @click="onGestureClick"
      >
        <p v-if="gestureOn">Turn Off Gesture Control</p>
        <p v-else>Turn On Gesture Control</p>
      </v-btn>
    </v-app>
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
  background-color: #264653;
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
