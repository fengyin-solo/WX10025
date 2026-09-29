import { createRouter, createWebHistory } from 'vue-router'

import Dashboard from '@/views/Dashboard.vue'
const Route = () => import('@/views/route/index.vue')
const Vehicle = () => import('@/views/vehicle/index.vue')
const Driver = () => import('@/views/driver/index.vue')
const Task = () => import('@/views/task/index.vue')
const Transfer = () => import('@/views/transfer/index.vue')
const Landfill = () => import('@/views/landfill/index.vue')
const Weight = () => import('@/views/weight/index.vue')
const Leachate = () => import('@/views/leachate/index.vue')
const Monitor = () => import('@/views/monitor/index.vue')
const Hazardous = () => import('@/views/hazardous/index.vue')
const Gps = () => import('@/views/gps/index.vue')
const Fuel = () => import('@/views/fuel/index.vue')
const Overload = () => import('@/views/overload/index.vue')
const Complaint = () => import('@/views/complaint/index.vue')
const Container = () => import('@/views/container/index.vue')
const Compress = () => import('@/views/compress/index.vue')

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'dashboard', component: Dashboard },
    { path: '/route', name: 'route', component: Route },
    { path: '/vehicle', name: 'vehicle', component: Vehicle },
    { path: '/driver', name: 'driver', component: Driver },
    { path: '/task', name: 'task', component: Task },
    { path: '/transfer', name: 'transfer', component: Transfer },
    { path: '/landfill', name: 'landfill', component: Landfill },
    { path: '/weight', name: 'weight', component: Weight },
    { path: '/leachate', name: 'leachate', component: Leachate },
    { path: '/monitor', name: 'monitor', component: Monitor },
    { path: '/hazardous', name: 'hazardous', component: Hazardous },
    { path: '/gps', name: 'gps', component: Gps },
    { path: '/fuel', name: 'fuel', component: Fuel },
    { path: '/overload', name: 'overload', component: Overload },
    { path: '/complaint', name: 'complaint', component: Complaint },
    { path: '/container', name: 'container', component: Container },
    { path: '/compress', name: 'compress', component: Compress },
  ],
})

export default router
