import {createRouter, createWebHistory} from 'vue-router'
import store from "@/store";
import LoginView from '../pages/LoginView.vue'
import RegisterView from '../pages/RegisterView.vue'
import FightView from '../pages/FightView.vue'

const routes = [
  {
    path: '/',
    name: 'login',
    meta: {
      needAuth: false,
    },
    component: LoginView
  },
  {
    path: '/register',
    name: 'register',
    meta: {
      needAuth: false,
    },
    component: RegisterView
  },
  {
    path: '/fights',
    name: 'fights',
    meta: {
      needAuth: true,
    },
    component: FightView,
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach(
  async (to, from, next) => {
    let needAuth = to.matched.some(route => route.meta.needAuth)
    let isAuth = store.getters.isAuth

    console.log('needAuth', needAuth)
    console.log('isAuth', isAuth)

    if (needAuth && !isAuth) {
      next({name: 'login'})
    } else {
      if (!needAuth && isAuth) {
        next({name: 'fights'})
      }
      next()
    }
  }
)

export default router
