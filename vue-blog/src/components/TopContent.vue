<!-- 参考にしたページ https://www.dailyupblog.com/web_development/742/ -->
<template>
  <main>
    <h2>{{ title }}</h2>
  </main>
</template>

<script lang="ts">
export default {
  data() {
    return {
      title: "TOPページです。",
    };
  },
};
</script>

<style scoped>
main {
  height: calc(100vh - 152px);
  padding: 3% 0;
  box-sizing: border-box;
  display: flex;
  justify-content: center;
  align-items: center;
}
h2 {
  margin: 0;
}
</style>
