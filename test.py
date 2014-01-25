import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<html>')
def hello(html):
	return render_template(html)

if __name__== '__main__':
	app.run()