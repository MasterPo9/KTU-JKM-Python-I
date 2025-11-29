from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
kakas = 0


@app.route('/')
def index():
    return render_template('index_ajax.html')


@app.route('/action-json', methods=['POST'])
def action_json():
    global kakas
    data = request.get_json() or {}
    btn = data.get('button')
    # do processing
    if btn == "btn1":
        try:
            kakas -= 1
        except ValueError:
            kakas = 0
    if btn == "btn2":
        try:
            kakas += 1
        except ValueError:
            kakas = 0
    result = f"Server received: {btn}\n{kakas}"
    return jsonify(result=result)


if __name__ == '__main__':
    app.run(debug=True)
