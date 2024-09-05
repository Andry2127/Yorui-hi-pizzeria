from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu')
def menu():
    pizza_data = {
        'pizza1_price': 120,
        'pizza_Yoruichi_price': 200,
        'pizza_IT_price': 160
    }
    return render_template('menu.html', **pizza_data)

if __name__ == '__main__':
    app.run(debug=True)
