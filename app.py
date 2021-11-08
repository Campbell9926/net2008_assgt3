from flask import Flask

app = Flask(__name__)

@app.route('/')

def home():
    return 'Home Page'

@app.route('/interfaces')
def interfaces():
    d["int_name"] = "ip-address"
    res = make_response(jsonify(d), 200)
    return res

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
