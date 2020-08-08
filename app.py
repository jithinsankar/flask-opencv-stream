from flask import Flask, render_template, Response, request
import cv2
import json

app = Flask(__name__)
video = cv2.VideoCapture(0)

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')

def gen():
    """Video streaming generator function."""
    while True:
        rval, frame = video.read()
        cv2.imwrite('t.jpg', frame)
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + open('t.jpg', 'rb').read() + b'\r\n')

@app.route('/direction', methods=['POST'])
def direction():
    dir = (request.form['dir'])
    if dir  == 'front' :
        print("front") #insert command for front here
    if dir  == 'left' :
        print("left")  #insert command for left here
    if dir  == 'right' :
        print("right") #insert command for right here
    if dir  == 'back' :
        print("back")  #insert command for back here

    return json.dumps({'status':'OK'});

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(),mimetype='multipart/x-mixed-replace; boundary=frame')
