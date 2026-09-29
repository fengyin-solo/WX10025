<template>
  <div class="app-shell">
    <aside class="app-side">
      <h1 class="app-title">固废收运处理管理平台</h1>
      <nav class="nav-list">
        <RouterLink v-for="item in navItems" :key="item.path" :to="item.path" class="nav-item">
          {{ item.label }}
        </RouterLink>
      </nav>
    </aside>
    <main class="app-main">
      <header class="app-head">
        <span class="head-desc">面向收运路线规划、收运车辆调度、中转站管理、填埋场管理、渗滤液处理、称重计量与环保监测的一体化固废收运处理管理后台。</span>
        <span class="head-user">当前值班：{{ store.operator }} · {{ store.shiftLabel }}</span>
      </header>
      <RouterView />
    </main>
  </div>
</template>

<script setup lang="ts">
import { useSessionStore } from '@/stores/session'

const store = useSessionStore()

const navItems = [{ label: "运营概览", path: "/" }, { label: "收运路线管理", path: "/route" }, { label: "收运车辆管理", path: "/vehicle" }, { label: "驾驶员管理", path: "/driver" }, { label: "收运任务管理", path: "/task" }, { label: "中转站管理", path: "/transfer" }, { label: "填埋场管理", path: "/landfill" }, { label: "称重计量管理", path: "/weight" }, { label: "渗滤液处理", path: "/leachate" }, { label: "环保监测", path: "/monitor" }, { label: "有害垃圾管理", path: "/hazardous" }, { label: "车辆GPS监控", path: "/gps" }, { label: "油耗管理", path: "/fuel" }, { label: "超载管理", path: "/overload" }, { label: "市民投诉", path: "/complaint" }, { label: "收集容器管理", path: "/container" }, { label: "压缩设备管理", path: "/compress" }]
</script>
