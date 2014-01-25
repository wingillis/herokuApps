import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/<html>')
def hello(html=None):
	if not html:
		return "Hello world!"
	else:
		return render_template(html +'.html')

if __name__== '__main__':
	app.run()