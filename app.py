from flask import Flask, jsonify, make_response

app = Flask(__name__)

@app.route('/')

def home():
    return 'Home Page'

@app.route('/interfaces')
def interfaces():
    d = {}
    dd= {}
    with open("interfaces.txt", "r") as file:
        readlines = file.readlines()
        for line in readlines:
            words = line.split(" ")
            for word in words:
                if word.startswith("addr"):
                    word = word.split(":")
                    d[words[0]] = word[1]
                    break

        dd["ComputerInterfaces"] = d

    return dd

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
