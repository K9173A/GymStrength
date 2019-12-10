import Vue from 'vue';

import Router from 'vue-router';

import store from '@/storage/index';


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
      component: () => import('./views/Plan.vue'),
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

router.beforeEach((to, from, next) => {
  if (to.meta.requiresAuth) {
    if (store.getters.getAccessToken) {
      if (store.dispatch('verifyToken')) {
        next();
      } else {
        if (store.dispatch('refreshToken')) {
          next();
        } else {
          next({ name: 'login' });
        }
      }
    } else {
      next({ name: 'registration' });
    }
  }
});

export default router;
