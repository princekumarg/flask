from flask import Flask
app=Flask(__name__)
@app.route('/pri')
def hello_world():
    return '<h1>Hello world biggger prince</h1>'