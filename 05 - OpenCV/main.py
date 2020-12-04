# main.py
# import the necessary packages
from flask import Flask, render_template, Response
from camera import VideoCamera

import base64
import io
from matplotlib.figure import Figure

import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    # rendering webpage
    return render_template('index.html')


def gen(camera):
    while True:
        #get camera frame
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg' 
               b'\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera(1920,1080)),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

def plot_to_html(fig):
    # Encode the image. You don't have to change this.
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    # Embed the result in the html output.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return f'data:image/png;base64,{data}'

@app.route('/matplotlib')
def matplotlib():

    # Create a figure (doesn't matter what it contains).
    fig = Figure()
    ax = fig.subplots()
    x = np.arange(0, 10, 0.1)
    ax.plot(np.sin(x), np.cos(x))
    ax.set_title("O")
    ax.axis('equal')

    x = [0, 0, 1, 2, 2]
    y = [1, 0, 0.75, 0, 1]
    fig2 = Figure()
    ax2 = fig2.subplots()
    ax2.plot(x,y)
    ax2.set_title("W")
    ax2.axis('equal')

    figs = [plot_to_html(fig) for fig in [fig2, fig, fig2]]
    return render_template('plots.html', plots=figs)

if __name__ == '__main__':
    # defining server ip address and port
    app.run()