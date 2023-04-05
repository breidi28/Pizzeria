from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

orders = []

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/mario.html')
@app.route('/mario')
def mario():
    return render_template('mario.html')

@app.route('/submit_pizzas', methods=['POST'])
def submit_pizzas():
    selected_pizzas = request.form.getlist('pizzas[]')
    orders.append({"id": len(orders)+1, "selected_pizzas": selected_pizzas})
    return redirect(url_for('luigi'))

@app.route('/luigi.html')
@app.route('/luigi')
def luigi():
    return render_template('luigi.html', orders=orders)

if __name__ == '__main__':
    app.run(debug=True)