/**
 * plugins/vuetify.ts
 *
 * Framework documentation: https://vuetifyjs.com`
 */

// Vuetify 3
// https://next.vuetifyjs.com/en/getting-started/installation/#manual-steps
import "@mdi/font/css/materialdesignicons.css"; // mdi font
import "vuetify/styles";
import { createVuetify } from "vuetify";
import * as components from "vuetify/components";
import * as directives from "vuetify/directives";
// Vuetify Labs
// https://vuetifyjs.com/en/labs/introduction/
import * as labs from "vuetify/labs/components";

export const vuetify3 = createVuetify({
  components: {
    ...components,
    ...labs,
  },
  directives,
});
