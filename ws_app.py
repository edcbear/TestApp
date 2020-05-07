# date : 2020/5/6 18:58     
import json

from geventwebsocket.websocket import WebSocket
from geventwebsocket.server import WSGIServer
from geventwebsocket.handler import WebSocketHandler

from flask import Flask, request

app = Flask(__name__)

socket_dict = {}


@app.route("/app/<username>")
def app_ws(username):
    sock = request.environ.get("wsgi.websocket")  # type:WebSocket
    if not sock:
        return "请使用Websocket客户端连接"
    socket_dict[username] = sock
    print(socket_dict)
    while True:
        msg = sock.receive()
        msg_dict = json.loads(msg)
        receiver = msg_dict.get("receiver")
        recv_sock = socket_dict.get(receiver)
        recv_sock.send(msg)



if __name__ == '__main__':
    http_serv = WSGIServer(("192.168.1.101", 9528), app, handler_class=WebSocketHandler)
    http_serv.serve_forever()
