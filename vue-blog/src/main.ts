import { createApp } from "vue";
import { createPinia } from "pinia";

import App from "./App.vue";
import router from "./router";

// Vuetify 3
// https://next.vuetifyjs.com/en/getting-started/installation/#manual-steps
import "vuetify/styles";
import { createVuetify } from "vuetify";
import * as components from "vuetify/components";
import * as directives from "vuetify/directives";
import labs from "./plugins/vuetify";
import "@mdi/font/css/materialdesignicons.css"; // この行を追加

// assets
import "./assets/main.css";

const vuetify = createVuetify({
  components,
  directives,
});

const app = createApp(App);

app.use(createPinia());
app.use(router);
app.use(vuetify);
app.use(labs);

app.mount("#app");
