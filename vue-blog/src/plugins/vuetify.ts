/**
 * plugins/vuetify.ts
 *
 * Framework documentation: https://vuetifyjs.com`
 */
import { createVuetify } from "vuetify";
import * as labs from "vuetify/labs/components";

export default createVuetify({
  components: {
    ...labs,
  },
});
