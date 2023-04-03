from flask import Flask, render_template

app = Flask(__name__)

app.route('/')
app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/pickup')
def pickup():
    return render_template('pickup.html')

@app.route('/delivery')
def delivery():
    return render_template('delivery.html')

@app.route('/deliverypostscreen')
def deliverypostscreen():
    return render_template('deliverypostscreen.html')

@app.route('/pickuppostscreen')
def pickuppostscreen():
    return render_template('pickuppostscreen.html')

if __name__ == '__main__':
    app.run(debug=True)