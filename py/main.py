from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
cors = CORS(app)

# MongoDB connection URL
client = MongoClient('mongodb://192.168.1.20:49153/')
db = client['sample_geospatial']  # Replace with your database name

@app.route('/api/shipwrecks', methods=['GET'])
def get_shipwrecks():
    try:
        shipwrecks = list(db['near_durham'].find({}, {'_id': 0, 'coordinates': 1}))
        return jsonify(shipwrecks)
    except Exception as e:
        return jsonify(error=str(e)), 500

if __name__ == '__main__':
    app.run(debug=True)
