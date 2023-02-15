<!-- 参考にしたページ https://www.dailyupblog.com/web_development/742/ -->
<template>
  <header>
    <h1>{{ title }}</h1>
  </header>
</template>

<script lang="ts">
export default {
  data() {
    return {
      title: "ヘッダー",
    };
  },
};
</script>

<style scoped>
header {
  padding: 1em 0;
  background: #778899;
}
h1 {
  margin: 0;
  color: #fff;
}
</style>
