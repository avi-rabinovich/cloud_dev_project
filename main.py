print("starting app")


from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Everybody!'


@app.route('/mimi/')
def hello_mimi():
    return 'Hello, Mimi!'



app.run(debug=True)
