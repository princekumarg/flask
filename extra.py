from flask import Flask
app=Flask(__name__)
@app.route('/')
def hello_world():
    return '<h1>Hello world biggger prince</h1>'
@app.route('/about')
def about_page():
    return '<h1>About Page<h1>'