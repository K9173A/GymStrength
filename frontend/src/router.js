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
      path: '/gym',
      name: 'plan',
      meta: { requiresAuth: true },
      component: () => import('./views/Index.vue'),
    },
    {
      path: '/calculators',
      name: 'calculators',
      props: true,
      component: () => import('./views/Calculator.vue'),
    },
    {
      path: '/register',
      name: 'registration',
      component: () => import('./views/Registration.vue'),
    },
    {
      path: '*',
      redirect: '/',
    },
  /*
    {
      path: '/activate/:uid/:token',
      name: 'activation',
      props: true,
      component: () => import('./views/Activate.vue'),
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('./components/form/Login.vue'),
    },
  */
  ],
});

export default router;
