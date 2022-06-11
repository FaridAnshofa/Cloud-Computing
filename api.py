from flask import Flask, jsonify
import function as fs

# GET
# name = request.args.get('name')
# POST
# record = json.loads(request.data)
app = Flask(__name__)
defaultMsg = {'status': 'success','message': 'Please refrence to endpoint !'}
@app.route('/')
def index():
    return jsonify(defaultMsg)
@app.route('/api')
def api():
    return jsonify(defaultMsg)

@app.route('/api/literature', methods=['GET'])
def literature():
    try:
        return jsonify({'error': False, 'message': 'Literature fetch successfully ', 'literature': fs.documentList('literature')})
    except:
        return jsonify({'error': True,'message':'Literature fetch failed ','literature': ""})


app.run(host="localhost", port=5000, debug=True)

