import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import SignUpView from "../views/SignUpView.vue";
import PatientView from "../views/PatientView.vue";

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignUpView
  },
  {
    path: '/patient',
    name: 'patient',
    component: PatientView
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
