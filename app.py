
from flask import Flask, render_template, request, redirect


# app
app = Flask(__name__)


# app secret key
app.secret_key = "anything"

# Login
@app.route('/login', methods=["GET", "POST"])
def login():
   return render_template('index.html')


@app.route('/', methods=['GET'])
def base():
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
