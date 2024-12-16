from flask import Flask, render_template

app = Flask(__name__)

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for the cards page
@app.route('/cards')
def cards():
    return render_template('cards.html')

if __name__ == '__main__':
    app.run(debug=True)
