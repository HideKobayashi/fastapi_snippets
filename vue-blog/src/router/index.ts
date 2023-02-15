import { createRouter, createWebHistory } from "vue-router";
import BlogView from "../views/BlogView.vue";
import TopView from "../views/TopView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "top",
      component: TopView,
    },
    {
      path: "/blog/list",
      name: "bloglist",
      component: BlogView,
    },
  ],
});

export default router;
