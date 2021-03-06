from flask import Flask
from flask import render_template
from flask import Response

#import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)

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
    if direction == "f":
        GPIO.output(18, GPIO.HIGH)
        GPIO.output(15, GPIO.HIGH)
        GPIO.output(14, GPIO.LOW)
        GPIO.output(24, GPIO.LOW)
        GPIO.output(25, GPIO.LOW)
    elif direction == "fl":
        GPIO.output(18, GPIO.HIGH)
        GPIO.output(15, GPIO.HIGH)
        GPIO.output(14, GPIO.LOW)
        GPIO.output(24, GPIO.HIGH)
        GPIO.output(25, GPIO.LOW)
    elif direction == "fr":
        GPIO.output(18, GPIO.HIGH)
        GPIO.output(15, GPIO.HIGH)
        GPIO.output(14, GPIO.LOW)
        GPIO.output(24, GPIO.LOW)
        GPIO.output(25, GPIO.HIGH)
    elif direction == "b":
        GPIO.output(18, GPIO.HIGH)
        GPIO.output(14, GPIO.HIGH)
        GPIO.output(15, GPIO.LOW)
        GPIO.output(24, GPIO.LOW)
        GPIO.output(25, GPIO.LOW)
    elif direction == "bl":
        GPIO.output(18, GPIO.HIGH)
        GPIO.output(14, GPIO.HIGH)
        GPIO.output(15, GPIO.LOW)
        GPIO.output(24, GPIO.HIGH)
        GPIO.output(25, GPIO.LOW)
    elif direction == "br":
        GPIO.output(18, GPIO.HIGH)
        GPIO.output(14, GPIO.HIGH)
        GPIO.output(15, GPIO.LOW)
        GPIO.output(24, GPIO.LOW)
        GPIO.output(25, GPIO.HIGH)
    elif direction == "off":
        GPIO.output(18, GPIO.LOW)
        GPIO.output(15, GPIO.LOW)
        GPIO.output(14, GPIO.LOW)
        GPIO.output(24, GPIO.LOW)
        GPIO.output(25, GPIO.LOW)

    return Response("{\"direction\":\""+direction+"\"}", status=200, mimetype='application/json')
