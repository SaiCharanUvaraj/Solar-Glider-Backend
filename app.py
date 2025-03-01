from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*") 

@socketio.on('sensor_data')
def handle_sensor_data(data):
    print(f"Received sensor data: {data}") 
    socketio.emit('ack', {"status": "Data received"})  

@app.route('/')
def index():
    return "WebSocket Server is Running!"

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)
