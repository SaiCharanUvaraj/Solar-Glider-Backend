from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*") 

latest_sensor_data = {"message": "No data received yet"}

@socketio.on('sensor_data')
def handle_sensor_data(data):
    global latest_sensor_data
    latest_sensor_data = data
    socketio.emit('update_data', latest_sensor_data)
    
@app.route('/')
def index():
    return render_template("index.html") 

if __name__ == "__main__":
    socketio.run(app, port=5000, debug=True)