from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.json
        return {'message': 'Запрос успешно обработан'}
    return 'Добро пожаловать на сервер Flask!'

if __name__ == '__main__':
	app.run(debug=True, host='127.0.0.1', port=5001)