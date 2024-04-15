from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world ():
    return "Hello World"

@app.route('/login')
def hello_world ():
    return "Hello World from login page"

@app.route('/signup')
def signup_here ():
    return "Hello World from signup page"

@app.route('/bye')
def bye():
    c = 2*500
    s = str(c)
    return "bye"

if __name__=="__main__":
    app.run()
    
if __name__=="__main__":
    app.run(host="127.0.0.1", port=80)
