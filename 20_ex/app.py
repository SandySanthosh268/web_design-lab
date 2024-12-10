from flask import Flask, render_template, request
import RPi.GPIO as GPIO

app = Flask(__name__)

# Setup GPIO
GPIO.setmode(GPIO.BCM)
relay_pin = 17  # GPIO pin connected to the relay
GPIO.setup(relay_pin, GPIO.OUT)
GPIO.output(relay_pin, GPIO.HIGH)  # Relay off initially

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/toggle", methods=["POST"])
def toggle():
    state = request.form["state"]
    if state == "on":
        GPIO.output(relay_pin, GPIO.LOW)  # Turn relay on
    else:
        GPIO.output(relay_pin, GPIO.HIGH)  # Turn relay off
    return "OK"

if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0", port=5000)
    except KeyboardInterrupt:
        GPIO.cleanup()
