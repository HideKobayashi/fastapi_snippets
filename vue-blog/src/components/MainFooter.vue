<!-- 参考にしたページ https://www.dailyupblog.com/web_development/742/ -->
<template>
  <footer>
    <div>
      <p>{{ msg }}</p>
    </div>
  </footer>
</template>

<script lang="ts">
export default {
  data() {
    return {
      msg: "フッター",
    };
  },
};
</script>

<style scoped>
footer {
  background: #dcdcdc;
  padding: 0.5em 0;
}
</style>
