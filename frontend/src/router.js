import Vue from 'vue';

import Router from 'vue-router';

import store from '@/store/index';


Vue.use(Router);

const router = new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      component: () => import('./views/Index.vue'),
    },
    {
      path: '/workouts/?page=:page?',
      name: 'workouts',
      meta: { requiresAuth: true },
      component: () => import('./views/Workouts.vue'),
    },
    // {
    //   path: 'workout_exercises?page=:page',
    //   name: 'workoutExercises',
    //   meta: { requiresAuth: true },
    //   props: route => ({ page: route.params.page || 1 }),
    //   component: () => import('./views/WorkoutExercises.vue'),
    // },
    {
      path: '/exercises/:page?',
      name: 'databaseExercises',
      component: () => import('./views/ExercisesList.vue'),
    },
    {
      path: '/calculators',
      name: 'calculators',
      component: () => import('./views/Calculator.vue'),
    },
    {
      path: '/about',
      name: 'about',
      component: () => import('./views/About.vue'),
    },
    {
      path: '/users/register',
      name: 'registration',
      component: () => import('./views/Registration.vue'),
    },
    {
      path: '/users/login',
      name: 'login',
      component: () => import('./views/Login.vue'),
    },
    // {
    //   path: '/activate/:uid/:token',
    //   name: 'activation',
    //   props: true,
    //   component: () => import(),
    // },
    {
      path: '*',
      redirect: '/',
    },
  ],
});

router.beforeEach((to, from, next) => {
  if (to.meta.requiresAuth) {
    if (store.getters.getAccessToken) {
      if (store.dispatch('verifyToken') || store.dispatch('refreshToken')) {
        next();
      } else {
        next({ name: 'login' });
      }
    } else {
      next({ name: 'registration' });
    }
  } else {
    next();
  }
});

export default router;
