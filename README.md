# 固废收运处理管理平台

面向收运路线规划、收运车辆调度、中转站管理、填埋场管理、渗滤液处理、称重计量与环保监测的一体化固废收运处理管理后台。

这是一个前后端分离的管理平台：前端 Vue 3 + Vite + TypeScript，后端 FastAPI（Python）。
两边各自独立启动，前端 dev server 已关掉自动打开页面，启动后按终端打印的地址手工打开。

## 目录结构

```text
.
├── frontend/                 Vue 3 + Vite + TypeScript 前端
│   ├── src/views/            每个业务模块一个页面
│   ├── src/api/              统一请求封装
│   ├── src/stores/           会话与筛选状态
│   └── vite.config.ts        dev server 配置（open: false）
├── backend/                  FastAPI（Python） 后端
│   ├── app/routers/          每个业务模块一组接口
│   ├── app/services/         业务规则与状态流转
│   └── app/store.py          内存数据仓库与示例数据
├── .gitignore
└── docker-compose.yml
```

## 启动

### 后端

```bash
cd backend
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
./run.sh
```

健康检查：`curl http://127.0.0.1:8000/api/health`

### 前端

```bash
cd frontend
npm install
npm run dev
```

前端默认监听 `http://127.0.0.1:5173/`，dev server 不会自动打开浏览器，
需要自己访问。`/api` 由 vite 代理到后端 `http://127.0.0.1:8000`。

## 业务模块

| 模块 | 目录 | 业务对象 | 主要字段 |
| --- | --- | --- | --- |
| 收运路线管理 | `route` | 收运路线 | 路线编号、路线名称、起点中转站 |
| 收运车辆管理 | `vehicle` | 收运车辆 | 车牌号、车辆类型、核定载重 |
| 驾驶员管理 | `driver` | 驾驶员 | 工号、姓名、驾驶证类型 |
| 收运任务管理 | `task` | 收运任务 | 任务编号、收运路线、收运车辆 |
| 中转站管理 | `transfer` | 中转站 | 站号、站名、所在区域 |
| 填埋场管理 | `landfill` | 填埋场 | 场号、场名、总库容 |
| 称重计量管理 | `weight` | 称重记录 | 记录编号、车牌号、皮重 |
| 渗滤液处理 | `leachate` | 渗滤液处理站 | 站号、所属填埋场、设计处理量 |
| 环保监测 | `monitor` | 监测点位 | 点位编号、监测类型、所属场所 |
| 有害垃圾管理 | `hazardous` | 有害垃圾收集点 | 收集点编号、收集点位置、容器类型 |
| 车辆GPS监控 | `gps` | GPS终端 | 终端编号、绑定车辆、通信卡号 |
| 油耗管理 | `fuel` | 加油记录 | 记录编号、车辆牌照、加油日期 |
| 超载管理 | `overload` | 超载记录 | 记录编号、车牌号、标记载重 |
| 市民投诉 | `complaint` | 投诉记录 | 投诉编号、投诉来源、投诉类型 |
| 收集容器管理 | `container` | 收集容器 | 容器编号、容器类型、放置位置 |
| 压缩设备管理 | `compress` | 压缩设备 | 设备编号、设备类型、所属中转站 |

## 约定

- 每个模块的前端页面在 `frontend/src/views/<模块>/index.vue`，后端接口在
  `backend/app/routers/<模块>.py`，业务规则在 `backend/app/services/<模块>.py`。
- 列表接口统一返回 `{ items, total, page, size }`，动作接口统一返回 `{ ok, message }`。
- 状态流转只允许在 `app/services` 里改，路由层不做业务判断。
