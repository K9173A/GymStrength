import Vue from 'vue';

import Router from 'vue-router';


Vue.use(Router);

const router = new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      component: () => import('./views/Index.vue'),
    },
    {
      path: '/',
      name: 'plan',
      component: () => import('./views/Index.vue'),
    },
  ],
});

export default router;
