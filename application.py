from flask import Flask, render_template
from flask_socketio import SocketIO, send

application = Flask(__name__)
application.config['SECRET_KEY'] = 'somesecret'
socketio = SocketIO(application)

@application.route('/')
def home():
    print('here')
    return render_template('index.html')


@socketio.on('message')
def handle_message(message):
    print('Message received: ' + message)
    if message != "User Connected":
        send(message, broadcast=True)


if __name__ == '__main__':
    socketio.run(application, debug=True)