import { createApp } from "vue";
import vuetify from "./plugins/vuetify";
import App from "./App.vue";

createApp(App)
  .use(vuetify)
  .mount("#app")
  .$nextTick(() => {
    // Remove Preload scripts loading
    postMessage({ payload: "removeLoading" }, "*");

    // Use contextBridge
    window.ipcRenderer.on("main-process-message", (_event, message) => {
      console.log(message);
    });
  });
