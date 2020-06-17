from flask import Flask
from flask import render_template
import subprocess,signal
import threading

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("sensor_monitor_web.html")

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080)