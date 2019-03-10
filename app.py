#!flask/bin/python
from flask import Flask, jsonify

app = Flask(__name__)

companies = [
    
        {
            'id': 1,
            'name': u'SuperDelivery',
            'availability': True
        },
        {
            'id': 2,
            'name': u'FastDelivery',
            'availability': False
        }
    
]


@app.route('/delivery/get_availability/<city>', methods=['GET'])
def get_availability(city):
    return jsonify(companies), 200


if __name__ == '__main__':
    app.run(debug=True, host=('0.0.0.0'))

# curl -i http://localhost:5000/delivery/get_availability/Bologna