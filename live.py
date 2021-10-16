from flask import Flask, jsonify
from threading import Thread

app = Flask(" ")

@app.route("/")
def home():
    return jsonify({"status":True})

def run():
    app.run(host="0.0.0.0",port=8000)

def live():
    t = Thread(target=run)
    t.start()
