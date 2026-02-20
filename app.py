from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

# Store names in memory
visitors = []

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to My Docker App!",
        "student_app": True,
        "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

@app.route('/api/visitors', methods=['GET'])
def get_visitors():
    return jsonify({
        "visitors": visitors,
        "count": len(visitors)
    })

@app.route('/api/visitors', methods=['POST'])
def add_visitor():
    data = request.get_json()
    name = data.get('name', 'Anonymous')
    visitors.append({
        "name": name,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    return jsonify({
        "message": f"Welcome {name}!",
        "total_visitors": len(visitors)
    }), 201

@app.route('/api/hello')
def hello():
    name = request.args.get('name', 'Friend')
    return jsonify({
        "greeting": f"Hello, {name}!",
        "message": "You successfully called the API!"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)