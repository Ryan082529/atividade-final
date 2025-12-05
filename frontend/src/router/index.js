import { createRouter, createWebHistory } from 'vue-router'
import App from '../App.vue'

const routes = [
  { path: '/', name: 'home', component: App },
  { path: '/privado', name: 'privado', component: App, meta: { requiresAuth: true } }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

router.beforeEach((to, from, next) => {
  const requires = to.meta?.requiresAuth
  const token = localStorage.getItem('access_token')
  if (requires && !token) {
    return next({ name: 'home' })   
  }
  next()
})

export default router
