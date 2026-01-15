from flask import Flask, jsonify, render_template
from datetime import datetime, timedelta

app = Flask(__name__)

# Global variable to store current time
current_time = datetime.now()

@app.route('/')
def index():
    """Display main page with clock"""
    return render_template('index.html')

@app.route('/get_time')
def get_time():
    """Return current time in JSON format"""
    return jsonify({'time': current_time.strftime('%H:%M:%S')})

@app.route('/update_time', methods=['POST'])
def update_time():
    """Decrement time by 1 second"""
    global current_time
    current_time = current_time - timedelta(seconds=1)
    return jsonify({
        'status': 'success',
        'time': current_time.strftime('%H:%M:%S')
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
