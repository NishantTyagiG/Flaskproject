from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/health")
def liveness_probe():
    return {'status': 'alive'}, 200

@app.route("/test")
def Final():
    return render_template("hello.html")


app.run(host="0.0.0.0",port=3000)



