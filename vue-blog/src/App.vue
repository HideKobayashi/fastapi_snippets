<!-- 参考にしたページ https://www.dailyupblog.com/web_development/742/ -->
<template>
  <div id="app">
    <MainHeader />
    <RouterView />
    <MainFooter />
  </div>
</template>

<script lang="ts">
import MainHeader from "./components/MainHeader.vue";
import MainFooter from "./components/MainFooter.vue";
import { RouterView } from "vue-router";

export default {
  components: {
    MainHeader,
    RouterView,
    MainFooter,
  },
};
</script>

<style>
body {
  margin: 0;
}
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
