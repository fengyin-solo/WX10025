"""接口出入参模型：列表分页、动作结果与各模块的明细结构。"""
from __future__ import annotations

from typing import Any, Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class PageResult(BaseModel, Generic[T]):
    items: list[T]
    total: int
    page: int = 1
    size: int = 20


class ActionResult(BaseModel):
    ok: bool
    message: str
    entry: dict[str, Any] | None = None


class EntryPayload(BaseModel):
    """登记或修改一条业务记录时提交的字段集合。"""

    values: dict[str, Any] = Field(default_factory=dict)
    remark: str | None = None



class RouteEntry(BaseModel):
    """收运路线明细结构。"""

    field_0: str | None = None  # 路线编号
    field_1: str | None = None  # 路线名称
    field_2: str | None = None  # 起点中转站
    field_3: str | None = None  # 终点处理厂
    field_4: str | None = None  # 收运片区
    field_5: str | None = None  # 单程里程
    field_6: str | None = None  # 预计耗时
    field_7: str | None = None  # 路线状态

class VehicleEntry(BaseModel):
    """收运车辆明细结构。"""

    field_0: str | None = None  # 车牌号
    field_1: str | None = None  # 车辆类型
    field_2: str | None = None  # 核定载重
    field_3: str | None = None  # 所属单位
    field_4: str | None = None  # 发动机号
    field_5: str | None = None  # 年检日期
    field_6: str | None = None  # 保险到期
    field_7: str | None = None  # 车辆状态

class DriverEntry(BaseModel):
    """驾驶员明细结构。"""

    field_0: str | None = None  # 工号
    field_1: str | None = None  # 姓名
    field_2: str | None = None  # 驾驶证类型
    field_3: str | None = None  # 联系电话
    field_4: str | None = None  # 所属车队
    field_5: str | None = None  # 从业资格证号
    field_6: str | None = None  # 上次体检日期
    field_7: str | None = None  # 人员状态

class TaskEntry(BaseModel):
    """收运任务明细结构。"""

    field_0: str | None = None  # 任务编号
    field_1: str | None = None  # 收运路线
    field_2: str | None = None  # 收运车辆
    field_3: str | None = None  # 驾驶员
    field_4: str | None = None  # 计划出车时间
    field_5: str | None = None  # 实际出车时间
    field_6: str | None = None  # 收运结束时间
    field_7: str | None = None  # 任务状态

class TransferEntry(BaseModel):
    """中转站明细结构。"""

    field_0: str | None = None  # 站号
    field_1: str | None = None  # 站名
    field_2: str | None = None  # 所在区域
    field_3: str | None = None  # 设计日处理量
    field_4: str | None = None  # 当前日进站量
    field_5: str | None = None  # 压缩机数量
    field_6: str | None = None  # 建成投用日期
    field_7: str | None = None  # 运行状态

class LandfillEntry(BaseModel):
    """填埋场明细结构。"""

    field_0: str | None = None  # 场号
    field_1: str | None = None  # 场名
    field_2: str | None = None  # 总库容
    field_3: str | None = None  # 已填库容
    field_4: str | None = None  # 剩余库容
    field_5: str | None = None  # 填埋层数
    field_6: str | None = None  # 投用日期
    field_7: str | None = None  # 运行状态

class WeightEntry(BaseModel):
    """称重记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 车牌号
    field_2: str | None = None  # 皮重
    field_3: str | None = None  # 毛重
    field_4: str | None = None  # 净重
    field_5: str | None = None  # 称重时间
    field_6: str | None = None  # 称重员
    field_7: str | None = None  # 记录状态

class LeachateEntry(BaseModel):
    """渗滤液处理站明细结构。"""

    field_0: str | None = None  # 站号
    field_1: str | None = None  # 所属填埋场
    field_2: str | None = None  # 设计处理量
    field_3: str | None = None  # 日处理量
    field_4: str | None = None  # 处理后COD值
    field_5: str | None = None  # 处理后氨氮值
    field_6: str | None = None  # 排放标准
    field_7: str | None = None  # 运行状态

class MonitorEntry(BaseModel):
    """监测点位明细结构。"""

    field_0: str | None = None  # 点位编号
    field_1: str | None = None  # 监测类型
    field_2: str | None = None  # 所属场所
    field_3: str | None = None  # 监测指标
    field_4: str | None = None  # 标准限值
    field_5: str | None = None  # 上次实测值
    field_6: str | None = None  # 监测频率
    field_7: str | None = None  # 监测状态

class HazardousEntry(BaseModel):
    """有害垃圾收集点明细结构。"""

    field_0: str | None = None  # 收集点编号
    field_1: str | None = None  # 收集点位置
    field_2: str | None = None  # 容器类型
    field_3: str | None = None  # 收集物类别
    field_4: str | None = None  # 上次清运日期
    field_5: str | None = None  # 下次计划清运
    field_6: str | None = None  # 管理人员
    field_7: str | None = None  # 收集点状态

class GpsEntry(BaseModel):
    """GPS终端明细结构。"""

    field_0: str | None = None  # 终端编号
    field_1: str | None = None  # 绑定车辆
    field_2: str | None = None  # 通信卡号
    field_3: str | None = None  # 在线状态
    field_4: str | None = None  # 上次定位时间
    field_5: str | None = None  # 当前经纬度
    field_6: str | None = None  # 当前速度
    field_7: str | None = None  # 终端状态

class FuelEntry(BaseModel):
    """加油记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 车辆牌照
    field_2: str | None = None  # 加油日期
    field_3: str | None = None  # 加油量
    field_4: str | None = None  # 加油金额
    field_5: str | None = None  # 里程表读数
    field_6: str | None = None  # 百公里油耗
    field_7: str | None = None  # 加油站名称

class OverloadEntry(BaseModel):
    """超载记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 车牌号
    field_2: str | None = None  # 标记载重
    field_3: str | None = None  # 实际载重
    field_4: str | None = None  # 超载比例
    field_5: str | None = None  # 查处时间
    field_6: str | None = None  # 查处地点
    field_7: str | None = None  # 处理状态

class ComplaintEntry(BaseModel):
    """投诉记录明细结构。"""

    field_0: str | None = None  # 投诉编号
    field_1: str | None = None  # 投诉来源
    field_2: str | None = None  # 投诉类型
    field_3: str | None = None  # 投诉内容
    field_4: str | None = None  # 投诉时间
    field_5: str | None = None  # 处理人
    field_6: str | None = None  # 办结时间
    field_7: str | None = None  # 处理状态

class ContainerEntry(BaseModel):
    """收集容器明细结构。"""

    field_0: str | None = None  # 容器编号
    field_1: str | None = None  # 容器类型
    field_2: str | None = None  # 放置位置
    field_3: str | None = None  # 容器容积
    field_4: str | None = None  # 投用日期
    field_5: str | None = None  # 上次清洗日期
    field_6: str | None = None  # 缺损情况
    field_7: str | None = None  # 容器状态

class CompressEntry(BaseModel):
    """压缩设备明细结构。"""

    field_0: str | None = None  # 设备编号
    field_1: str | None = None  # 设备类型
    field_2: str | None = None  # 所属中转站
    field_3: str | None = None  # 额定处理能力
    field_4: str | None = None  # 投用日期
    field_5: str | None = None  # 上次维保日期
    field_6: str | None = None  # 当前运行状态
