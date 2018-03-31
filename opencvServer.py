from flask import Flask,Response,render_template
import socket
import base64
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def getstuff():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host = '0.0.0.0'
    port = 8888
    s.bind((host,port))
    s.listen(5)
    clientsocket,addr = s.accept()
    while True:
        frame = clientsocket.recv(1024)
	print(frame)
        if not frame:
            yield(b"--frame\r\n"b"Content-Type: image/jpeg\r\n\r\n"+pdata+ b"\r\n")

@app.route('/videostream')
def videostream():
    return Response(getstuff(),mimetype='multipart/x-mixed-replace;boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
