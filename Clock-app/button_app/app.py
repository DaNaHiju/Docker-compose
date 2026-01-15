from flask import Flask, render_template, jsonify
import requests
import os

app = Flask(__name__)

# Get clock_app URL from environment variable
CLOCK_APP_URL = os.getenv('CLOCK_APP_URL', 'http://localhost:5001')

@app.route('/')
def index():
    """Display main page with button"""
    return render_template('index.html')

@app.route('/decrement', methods=['POST'])
def decrement():
    """Send POST request to clock_app to decrement time"""
    try:
        response = requests.post(f'{CLOCK_APP_URL}/update_time')
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
