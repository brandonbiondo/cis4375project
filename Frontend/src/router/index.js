import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Inventory from '../views/Inventory.vue'
import Employee from '../views/Employee.vue'
import Vendor from "../views/Vendor.vue";
import Quote from '../views/Quote.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/inventory',
      name: 'inventory',
      component: Inventory
    },
    {
      path: '/Employee',
      name: 'Employee',
      component: Employee
    },
    {
      path: '/Vendor',
      name: 'Vendor',
      component: Vendor
    },
    {
      path: '/quote',
      name: 'quote',
      component: Quote
    },
  ]
})

export { router }
