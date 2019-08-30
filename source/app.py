import os
import socket

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/ip")
def ip():
    hostname = socket.gethostname()
    hello_target = os.environ.get('HELLO_TARGET', 'World')
    return 'Hello, {}, from {}!\n'.format(hello_target, hostname)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
