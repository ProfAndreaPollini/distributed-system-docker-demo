from flask import Flask
from flask_cors import CORS

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from urllib.parse import quote_plus

app = Flask(__name__)
CORS(app)

uri = "mongodb://%s:%s@%s" % (
    quote_plus("root"), quote_plus("root1234"), "mongo")
client = MongoClient(uri)
try:
    # The ping command is cheap and does not require auth.
    client.admin.command('ping')
except ConnectionFailure:
    print("Server not available")



@app.route("/")
def hello_world():
    db = client.notes
    ret = []
    for x in db.notes.find():
        obj = {
            "oid": str(x["_id"]),
            "content": x["content"],
            "ts": x["ts"].as_datetime(),
        }
        ret.append(obj)
    return ret


@app.route("/pippo")
def hello_world2():
    return "<p>Hello, World!</p>"
