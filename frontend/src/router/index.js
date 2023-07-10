import Vue from 'vue';
import Router from 'vue-router';
import Home from '@/components/Home';
import NotFound from '@/components/error-pages/NotFound';
import PostList from '@/components/blog/PostList.component'
import Post from '@/components/blog/Post.component'

Vue.use(Router);


export default new Router({
    mode: 'history',
    routes: [
        {
            path: '/',
            name: 'Home',
            component: Home
        },
        {
            path: '/blog/posts/:id',
            name: 'Post',
            component: Post
        },
        {
            path: '/blog/posts/',
            name: 'PostList',
            component: PostList
        },
        {
            path: '*',
            name: 'NotFound',
            component: NotFound
        }
    ]
});
