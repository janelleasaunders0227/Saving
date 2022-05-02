from venv import Flask

app = Flask(__name__)

http://localhost:5000/

@app.route('/')
def index():
    return "Hello World!"

if (__name__ == "__main__"):
    app.run()