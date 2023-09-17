<script setup lang="ts">
import { ref, onMounted } from "vue";

const isCameraOpen = ref(false);
const cameraRef = ref<HTMLVideoElement | null>(null);

onMounted(() => {
  cameraRef.value?.focus;
});

const emit = defineEmits<{
  (e: "connect", id: string): void;
}>();

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
      class="rounded-sm"
      ref="cameraRef"
      :width="450"
      :height="337"
      autoplay
      playsinline
    ></video>
  </div>
</template>
