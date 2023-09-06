from flask import Flask,jsonify
app = Flask(__name__)

info = [
    {"name":"sandhya","id":521,"status":"billable"},
    {"name":'sindhu',"id":522,"status":"non_billable"},
    {"name":'yasmin',"id": 523,"status":"billable"},
    {"name":'jyothi',"id": 524,"status":"billable"},
    {"name":'nabeela',"id": 525,"status":"non_billable"}
    ]


@app.route('/')
def index():
    return "hello all"


@app.route('/info', methods=['GET'])
def get_info():
    return jsonify({"info":info})


@app.route("/info/<int:id>", methods=['GET'])
def get(id):
    return jsonify({'id': info[id]})


if __name__ == "__main__":
    app.run(debug=True)

