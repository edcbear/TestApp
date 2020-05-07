from flask import Blueprint, request, jsonify

from setting import MongoDB, RET

user_bp = Blueprint("user_bp", __name__)

@user_bp.route("/register",methods=["POST"])
def register():
    # 获取FormData中的数据
    user_info = request.form.to_dict()
    # 将数据转换成字典 直接存放在MongoDB中
    res = MongoDB.users.insert_one(user_info)
    if res.inserted_id:
        RET["code"] = 0
        RET["msg"] = "注册成功"
        RET["data"] = {}
        return jsonify(RET)
    else:
        RET["code"] = 1
        RET["msg"] = "注册失败"
        RET["data"] = {}
        return jsonify(RET)

@user_bp.route("/login",methods=["POST"])
def login():
    login_info = request.form.to_dict()
    user_info = MongoDB.users.find_one(login_info)
    if not user_info:
        # 登录失败
        RET["code"] = 1
        RET["msg"] = "用户名密码错误"
        RET["data"] = {}

        return jsonify(RET)
    else:
        user_info["_id"] = str(user_info.get("_id"))
        user_info.pop("password") # 删除敏感字段

        RET["code"] = 0
        RET["msg"] = "登录成功"
        RET["data"] = user_info

        return jsonify(RET)