<!-- Based from:  https://dagomez.medium.com/vue-3-basics-camera-and-screenshot-component-ac9af7d902f2 -->

<script setup lang="ts">
import { ref, onMounted } from "vue";

const isCameraOpen = ref(false);
const cameraRef = ref<HTMLVideoElement | null>(null);

const ws = new WebSocket("ws://127.0.0.1:3000");

onMounted(() => {
  cameraRef.value?.focus();
});

const emit = defineEmits<{
  (e: "connect", id: string): void;
}>();

const canvas = document.createElement("canvas");
canvas.width = 620;
canvas.height = 400;
const ctx = canvas.getContext("2d");

const number = ref(0);

function createCamera() {
  const constraints = {
    audio: false,
    video: true,
  };
  navigator.mediaDevices
    .getUserMedia(constraints)
    .then((stream) => {
      if (cameraRef.value) {
        cameraRef.value.srcObject = stream;
        emit("connect", stream.id);
      }
    })
    .catch((error) => {
      alert(`${error}: The browser could not find a camera.`);
      emit("connect", "error");
    });
  setInterval(function () {
    if (ws.readyState != 1) clearInterval(1);
    if (ctx && cameraRef.value) {
      ctx.drawImage(cameraRef.value, 0, 0, canvas.width, canvas.height);

      const dataURI = canvas.toDataURL("image/jpeg");

      if (dataURI) ws.send(dataURI);
    }
  }, 100);
}

function removeCamera() {
  let tracks = (<MediaStream>cameraRef.value?.srcObject)?.getTracks();

  tracks.forEach((track) => {
    track.stop();
  });
}

function toggleCamera() {
  if (isCameraOpen.value) {
    isCameraOpen.value = false;
    removeCamera();
  } else {
    isCameraOpen.value = true;
    createCamera();
  }
}

toggleCamera();
</script>

<template>
  <!-- <v-btn class="button" @click="toggleCamera()">
    <span v-if="!isCameraOpen">Open Camera</span>
    <span v-else>Close Camera</span>
  </v-btn> -->
  <div class="d-flex flex-row justify-center">
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
</template>
