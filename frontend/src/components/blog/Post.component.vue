<template>
    <div v-if="post.id">
        <h6>{{post.published_date}}</h6>
        <h1>{{post.title}}</h1>
        <p>{{post.text}}</p>
        <img src="https://s.poembook.ru/theme/3d/8e/bd/0f15cec8213b70f8bb031b9df64ed2fcc16c3304.png" style="width: 50px; height: 50px; cursor: pointer;"> {{post.likes}}
    </div>
        <div v-else class="err">
        <h1>ОШИБКА!!! Пост не найден. Ты не заблудился?</h1>
    </div>
</template>
<script>
import BlogService from '@/api-services/blog.service';
export default {
    name: 'PostList',
    data() {
        return {
          post: {}
        };
    },
    created(){
        BlogService.get(this.$route.params.id).then((response) => {
            this.post = response.data;   //Передаём список и сортируем по дате
        });
    },
}
</script>
</script>
<style scoped>
p {
  text-align: justify;
}
.err {
    font-weight: bold;
    font-size: 50px;
    text-align: center;
    color:#f10b0b;
}
</style>
