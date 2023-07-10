<template>
  <p class="homeText">
    Добро пожаловать в блог Лёхи
  </p>
</template>
<script>
import BlogService from '@/api-services/blog.service';

export default {
  name: 'Home',
  created() {
    BlogService.getAll().then((response) => {
      console.log(response.data);
    }).catch((error) => {
      console.log(error.response.data);
    });
  }
};
</script>
<style scoped>.homeText{
    font-size: 35px;
    color: red;
    text-align: center;
    position: relative;
    top:30px;
    text-shadow: 2px 2px 2px gray;
}
</style>
