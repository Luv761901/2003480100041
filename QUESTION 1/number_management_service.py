import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/numbers', methods=['GET'])
def get_numbers():
    urls = request.args.getlist('url')
    unique_numbers = set()
    
    for url in urls:
        try:
            response = requests.get(url, timeout=0.5)
            if response.status_code == 200:
                data = response.json()
                if 'numbers' in data:
                    unique_numbers.update(set(data['numbers']))
        except requests.exceptions.RequestException:
            pass

    return jsonify({'numbers': sorted(list(unique_numbers))})

if __name__ == '__main__':
    app.run(host='localhost', port=8008)
