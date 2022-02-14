from flask import Flask
app = Flask(__name__)

from datetime import datetime

@app.route('/')
def hello_world():
    return 'Hello world!, this is the time app of dp3278, Duc Phi!'

@app.route('/time')
def time():
    now = datetime.utcnow()
    current_time = now.strftime("%H:%M:%S")
    return "CURRENT TIME (UTC) --> " + current_time, 200

app.run(host='0.0.0.0',
        port=8080,
        debug=True)

