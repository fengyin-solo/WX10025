"""业务模块路由汇总。

这里统一按别名导入再暴露 ROUTERS：模块名有可能和内置名撞车（某个业务模块就叫 dict、list
这种名字时），按名字直接 import 会把内置类型覆盖掉，函数注解在运行时求值就会报
'module' object is not subscriptable。
"""
from __future__ import annotations

from app.routers import route as router_route
from app.routers import vehicle as router_vehicle
from app.routers import driver as router_driver
from app.routers import task as router_task
from app.routers import transfer as router_transfer
from app.routers import landfill as router_landfill
from app.routers import weight as router_weight
from app.routers import leachate as router_leachate
from app.routers import monitor as router_monitor
from app.routers import hazardous as router_hazardous
from app.routers import gps as router_gps
from app.routers import fuel as router_fuel
from app.routers import overload as router_overload
from app.routers import complaint as router_complaint
from app.routers import container as router_container
from app.routers import compress as router_compress

ROUTERS = [router_route, router_vehicle, router_driver, router_task, router_transfer, router_landfill, router_weight, router_leachate, router_monitor, router_hazardous, router_gps, router_fuel, router_overload, router_complaint, router_container, router_compress]
