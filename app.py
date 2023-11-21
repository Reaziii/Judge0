from flask import Flask, request, jsonify
from flask_cors import CORS  
from judge.cpp.main import get_verdict
from utils.convert_to_single_line import convert_to_single_line
app = Flask(__name__)
CORS(app)
@app.route('/api', methods=['POST'])
def api():
    try:
        data = request.form
        code = data['code']
        checker = data['checker']
        input = data['input']
        submission_id = data['submission_id']
        timelimit = data['timelimit']
        memorylimit = data['memorylimit']
        verdict = get_verdict(convert_to_single_line(code), timelimit,  submission_id, memorylimit, input,convert_to_single_line(checker))
        return jsonify({'verdict' : verdict })
    except Exception as e:
        return jsonify({'error': str(e)})
if __name__ == '__main__':
    app.run(debug=True)
