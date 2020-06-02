from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
	return 'This is the home page (in the other branch)'

@app.route('/<name>')
def welcome(name=None):
	return 'Welcome {}, BAD to see you!'.format(name)

if __name__ == '__main__':
	app.run()