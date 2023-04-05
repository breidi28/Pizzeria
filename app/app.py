from flask import Flask, render_template
import pandas as pd
import requests

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/mario')
def mario():
    """This function will take the order from mario.html and send it to the server.
    It will also send the data to luigi.html to queue the orders on the dashboard."""
    # when a user chooses a pizza or multiple pizzas, the id of the pizza will be sent to the server and added to the order list
    # the list is then sent to the server to luiigi.html to be displayed on the dashboard
    # the order list will be a list of dictionaries
    # each dictionary will have the pizza name, id, and time to make
    order_list = []
    
    return render_template('mario.html')

@app.route('/luigi')
def luigi():
    return render_template('luigi.html')

if __name__ == '__main__':
    app.run(debug=True)