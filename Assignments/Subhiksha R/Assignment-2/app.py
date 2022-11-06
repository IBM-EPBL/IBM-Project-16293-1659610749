from flask import *

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/signUp')
def signup():
    return render_template('signup.html')

@app.route('/signIn')
def sigin():
    return render_template('signin.html')

@app.route('/about')
def blog():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)