from flask import Flask, render_template, request, session
import pandas as pd
import csv
import time

app = Flask(__name__)

pizzas = [
    {'index': 0, 'pizza_name': 'pepperoni', 'pizza_price': 12, 'pizza_id': 1, 'time_to_make': 3},
    {'index': 1, 'pizza_name': 'cheese', 'pizza_price': 10, 'pizza_id': 2, 'time_to_make': 3},
    {'index': 2, 'pizza_name': 'veggie', 'pizza_price': 11, 'pizza_id': 3, 'time_to_make': 3},
    {'index': 3, 'pizza_name': 'meat_lovers', 'pizza_price': 13, 'pizza_id': 4, 'time_to_make': 4},
    {'index': 4, 'pizza_name': 'vegan', 'pizza_price': 11, 'pizza_id': 5, 'time_to_make': 5},
    {'index': 5, 'pizza_name': 'quattro_formaggi', 'pizza_price': 12, 'pizza_id': 6, 'time_to_make': 5},
    {'index': 6, 'pizza_name': 'quattro_stagioni', 'pizza_price': 13, 'pizza_id': 7, 'time_to_make': 7},
    {'index': 7, 'pizza_name': 'supreme', 'pizza_price': 14, 'pizza_id': 8, 'time_to_make': 6},
    {'index': 8, 'pizza_name': 'tonno', 'pizza_price': 12, 'pizza_id': 9, 'time_to_make': 5}
]

orders = []

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/mario.html')
@app.route('/mario')
def mario():
    return render_template('mario.html', pizzas=pizzas)

@app.route('/submit_pizzas', methods=['POST'])
def submit_pizzas():
    orders = []
    for index, pizza in enumerate(pizzas):
        quantity = int(request.form[pizza['pizza_name'].replace(' ', '_')])
        if quantity > 0:
            time_left = pizza['time_to_make']
            orders.append({
                'index': len(orders) + 1,
                'pizza_name': pizza['pizza_name'],
                'quantity': quantity,
                'time_left': time_left
            })
    return render_template('luigi.html', orders=orders)

@app.route('/luigi.html')
@app.route('/luigi')
def luigi():
    return render_template('luigi.html', orders=orders)


if __name__ == '__main__':
    app.run(debug=True)