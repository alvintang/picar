from flask import Flask
from flask import render_template
from flask import Response

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/controller/')
def controller(name=None):
    return render_template('rc.html')

@app.route('/controller/<direction>', methods=['POST'])
def controller_dir(direction=None):
    print(direction)
    if direction == "forward":
        GPIO.output(18, GPIO.HIGH)
    elif direction == "backward":
        GPIO.output(18, GPIO.HIGH)
    elif direction == "off":
        GPIO.output(18, GPIO.LOW)

    return Response("{\"direction\":\""+direction+"\"}", status=200, mimetype='application/json') 
