from flask import Flask, render_template
from converter.currency import get_currencies

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my-secret-key'


@app.route('/', methods=['GET'])
def index():
    currencies = get_currencies()
    # GET запрос - просто возвращаем страницу с формой
    return render_template('index.html',
                           currencies=currencies,
                           result=None,
                           amount=None,
                           currency1='EUR',
                           currency2='USD')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
