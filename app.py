from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.xvovm.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta



@app.route('/')
def home():
    return render_template('index.html')

@app.route("/latte", methods=["POST"])
def latte_post():
    name_receive = request.form['name_give']
    loca_receive = request.form['loca_give']
    address_receive = request.form['address_give']
    tag_receive = request.form['tag_give']

    doc = {
        'name': name_receive,
        'loca': loca_receive,
        'address': address_receive,
        'tag': tag_receive
    }
    db.latte.insert_one(doc)
    return jsonify({'msg': '저장 완료!'})

@app.route("/latte", methods=["GET"])
def latte_get():
    latte_list = list(db.latte.find({}, {'_id': False}))
    return jsonify({'latte': latte_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)