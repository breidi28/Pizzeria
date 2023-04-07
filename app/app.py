from flask import Flask, render_template, request, g
import sqlite3

app = Flask(__name__)

pizzas = [
    {'pizza_name': 'pepperoni', 'pizza_price': 12, 'pizza_id': 1, 'time_to_make': 3},
    {'pizza_name': 'cheese', 'pizza_price': 10, 'pizza_id': 2, 'time_to_make': 3},
    {'pizza_name': 'veggie', 'pizza_price': 11, 'pizza_id': 3, 'time_to_make': 3},
    {'pizza_name': 'meat_lovers', 'pizza_price': 13, 'pizza_id': 4, 'time_to_make': 4},
    {'pizza_name': 'vegan', 'pizza_price': 11, 'pizza_id': 5, 'time_to_make': 5},
    {'pizza_name': 'quattro_formaggi', 'pizza_price': 12, 'pizza_id': 6, 'time_to_make': 5},
    {'pizza_name': 'quattro_stagioni', 'pizza_price': 13, 'pizza_id': 7, 'time_to_make': 7},
    {'pizza_name': 'supreme', 'pizza_price': 14, 'pizza_id': 8, 'time_to_make': 6},
    {'pizza_name': 'tonno', 'pizza_price': 12, 'pizza_id': 9, 'time_to_make': 5}
]

DATABASE = 'orders.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.cli.command('initdb')
def initdb_command():
    init_db()
    print('Initialized the database.')

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
    db = get_db()
    cursor = db.cursor()
    orders = []
    for pizza in pizzas:
        quantity = request.form.get(f'quantity_{pizza["pizza_id"]}')
        if quantity is not None and quantity.isdigit() and int(quantity) > 0:
            time_left = pizza['time_to_make']
            orders.append((pizza['pizza_name'], int(quantity), time_left))

    if orders:
        order_number = cursor.execute('SELECT COALESCE(MAX(order_number), 0) + 1 FROM orders').fetchone()[0]
        cursor.executemany('INSERT INTO orders (order_number, pizza_name, quantity, time_left) VALUES (?, ?, ?, ?)',
                           [(order_number, *order) for order in orders])
        db.commit()

    return render_template('luigi.html', orders=orders)

@app.route('/luigi.html')
@app.route('/luigi')
def luigi():
    db = get_db()
    cursor = db.cursor

    orders = cursor.execute('SELECT * FROM orders').fetchall()
    return render_template('luigi.html', orders=orders)

if __name__ == '__main__':
    app.run(debug=True)