# 数据库配置信息
from pymongo import MongoClient

MC = MongoClient()
MongoDB = MC["XGreen"]

# Return Info 配置
RET = {
    "code": 0,
    "msg": "",
    "data": {}
}
