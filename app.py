from flask import Flask, request
import socket

app = Flask(__name__)
    
@app.route("/")
def hello():
    return '<form action="/echo" method="GET"><input name="text"><input type="submit" value="Echo"></form>'
    
@app.route("/echo")
def echo():
    hostname = socket.gethostname()
    return "You said: " + request.args.get('text', '') +". My hostname is " + hostname + "."
    
    
if __name__ == "__main__":
    app.run()