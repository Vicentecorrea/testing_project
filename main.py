from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
	return 'This is the home page'

@app.route('/<name>')
def welcome(name=None):
	return 'Welcome {}, nice to see you!'.format(name)

if __name__ == '__main__':
	app.run()