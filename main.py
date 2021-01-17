from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

users = [{"name": "Juan", "age": 25},
		 {"name": "Fernanda", "age": 67},
		 {"name": "Rosa", "age": 24}]

@app.route('/')
def home():
	try:
		name = request.args.get('name')
		age = int(request.args.get('age'))
		users.append({"name": name, "age": age})
	except:
		pass
	# return 'This is the home page (in the other branch)'
	return render_template('home.html', users=users)

@app.route('/<name>')
def welcome(name=None):
	return jsonify(users)

@app.route('/products')
def get_products():
	with open("products.json") as json_file:
		products = json.load(json_file)
		return jsonify(products)

if __name__ == '__main__':
	app.run()