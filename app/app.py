from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/mario')
def mario():
    return render_template('mario.html')

@app.route('/luigi')
def luigi():
    return render_template('luigi.html')

@app.route('/submit_pizzas', methods=['POST'])
def submit_pizzas():
    return render_template('submit_pizzas.html')

if __name__ == '__main__':
    app.run(debug=True)