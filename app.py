from flask import Flask, request, jsonify, send_from_directory
from spoiler_model import is_spoiler

app = Flask(__name__)

@app.route('/')
def serve_index():
    return send_from_directory('static', 'index.html')

@app.route('/check_comment', methods=['POST'])
def check_comment():
    data = request.json
    comment = data.get('comment', '')
    if is_spoiler(comment):
        return jsonify({'spoiler': True, 'comment': comment})
    else:
        return jsonify({'spoiler': False, 'comment': comment})

if __name__ == '__main__':
    app.run(debug=True)
