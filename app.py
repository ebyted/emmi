from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/beauty')
def beauty():
    return render_template('beauty.html')

@app.route('/barrasa')
def barrasa():
    return render_template('barrasa.html')

if __name__ == '__main__':
    app.run(debug=True)
