from flask import Flask
from flask_cors import CORS
import socketio
import time
import eventlet
import eventHandler
import os

app = Flask(__name__, static_url_path='',
            static_folder='live-chat',
            template_folder='live-chat')
CORS(app)

# socketio server and settings
sio = socketio.Server(async_mode='eventlet', cors_allowed_origins='*')


@app.route("/")
def hello_world():
    return app.send_static_file('index.html')


# event handler
eventHandler.eventHandler(sio, time)

# wrap socketio with a WSGI/Flask application so that both app can be run with eventlet
# link https://python-socketio.readthedocs.io/en/latest/server.html#creating-a-server-instance
socketapp = socketio.WSGIApp(sio, app)

# start the socket.io server with the Flask application and eventlet as the async_mode server (default is gevent) and listen on port 5000 for connections from the client side (the browser) and run the server forever until the program is terminated with Ctrl+C in the terminal window where the server is running. The server will be running on http://localhost:5000 by default. You can change the port number to any other number you want. Socket.io will automatically detect the port number and connect to it. And, socketio will be running in the background and will not block the main thread of execution. So, you can run other code in the main thread of execution. In this case, we are running the Flask application in the main thread of execution. So, the Flask application will be running on http://localhost:5000 and socket.io will be running on http://localhost:5000/socket.io/ and the client side will be able to connect to both of them. Also, socketio will be running in a new spawn process for each connection. So, the server will be able to handle multiple connections at the same time. And then,work with Flask in normal way.
# we can use it with Django too, just put the code in the same file as the Django project and run it with the command: python manage.py runserver   (or python3 manage.py runserver). And then, work with Django in normal way.
eventlet.wsgi.server(eventlet.listen(('', 7444)), socketapp)
