from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    age = 16
    return render_template('index.html',age=age)

@app.route('/users')
def users():
    user_list = ['Alice', 'Bob', 'Charlie']
    return render_template('users.html', users=user_list)

if __name__ == "__main__":
    app.run(debug=True)