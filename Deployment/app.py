from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World"

@app.route("/submit")
def submit():
    return "Hello from submit page"

if __name__ == '__main__':
    app.run()
