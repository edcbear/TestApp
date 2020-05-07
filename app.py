from flask import Flask, render_template

from serv.upload import upload
from serv.users import user_bp

app = Flask(__name__)
app.config["DEBUG"] = True
app.register_blueprint(user_bp)
app.register_blueprint(upload)



@app.route("/")
def ws():
    return render_template("ws_client.html")

if __name__ == '__main__':
    app.run("192.168.1.101", 9527)