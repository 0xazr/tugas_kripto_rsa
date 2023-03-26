import { createApp, markRaw } from "vue";
import { createPinia } from "pinia";

// import './style.css'
// import "./index.css";

import App from "./App.vue";
import router from "./router";

const app = createApp(App);
const pinia = createPinia();

pinia.use(({ store }) => {
  store.router = markRaw(router);
});

app.use(router);
app.use(pinia);

app.mount("#app");
