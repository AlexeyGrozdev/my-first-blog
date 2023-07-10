<template>
  <div>
    <p>Это список постов в блоге.</p>
    <ul>
      <li v-for="item in posts">
      <p>Опубликовано: {{item.published_date}}</p>
      <h1><a href="" @click="$router.push('/blog/posts/' + item.id)">{{item.title}}</a></h1>
      <p>{{item.text}}</p>
      </li>
    </ul>
  </div>
</template>
<script>
import BlogService from '@/api-services/blog.service';
export default {
    name: 'PostList',
    data() {
        return {
          posts: []
        };
    },
    created(){
        BlogService.getAll().then((response) => {
            this.posts = response.data.sort((a,b) => (a.published_date>b.published_date) ? 1 : -1 ); //Передаём список и сортируем по дате
        });
    },

};
</script>
