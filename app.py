from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def index(name="Hara"):  # put application's code here
    name = request.args.get('name', name)
    return "Hello from {}".format(name)


if __name__ == '__main__':
    app.run()
