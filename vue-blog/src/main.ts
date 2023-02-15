import { createApp } from "vue";
import { createPinia } from "pinia";
import { vuetify3 } from "./plugins/vuetify";

import App from "./App.vue";
import router from "./router";

// assets
import "./assets/main.css";

const app = createApp(App);

app.use(createPinia());
app.use(router);
app.use(vuetify3);

app.mount("#app");
