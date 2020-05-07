# date : 2020/5/6 20:30     
import os

from flask import Blueprint, request, jsonify, send_file

from setting import MongoDB, RET

upload = Blueprint("upload",__name__)

@upload.route("/uploader",methods=["POST"])
def uploader():
    reco = request.files.get("reco") # FileStorage
    reco.save(reco.filename)
    os.system(f"ffmpeg -i {reco.filename} {reco.filename}.mp3")
    RET["code"] = 0
    RET["msg"] = "上传成功"
    RET["data"] = {"filename": f"{reco.filename}.mp3"}

    return jsonify(RET)

@upload.route("/get_chat/<filename>")
def get_chat(filename):
    return send_file(filename)
