from flask import Flask, render_template, request, jsonify, redirect
import json, requests
from datetime import date

app = Flask(__name__)

api_url = "https://api-python-classes.herokuapp.com"
# api_url = "http://localhost:8080"

@app.route('/', methods = ["GET"])
def home():
	products_request = requests.get("{}/products".format(api_url))
	products = products_request.json()
	return render_template('home.html', products=products)

@app.route('/<product_id>', methods = ["GET"])
def product_details(product_id=None):
	product_request = requests.get("{}/products/{}".format(api_url, product_id))
	comments_request = requests.get("{}/products/{}/comments".format(api_url, product_id))
	product = product_request.json()
	product_comments = comments_request.json()
	return render_template("product_details.html", product=product, 
		comments=product_comments, len=len, range=range)

@app.route('/rate_product', methods = ["POST"])
def rate_product():
	product_id = int(request.form['product_id'])
	score = int(request.form['score'])
	data = {"product_id": product_id, "score": score}
	headers = {'Content-type': "application/json"}
	requests.post("{}/rate_product".format(api_url), json=data, headers=headers)
	return redirect('/{}'.format(product_id))

@app.route('/create_comment', methods = ["POST"])
def create_comment():
	product_id = int(request.form['product_id'])
	author = request.form['author']
	text = request.form['text']
	today = date.today().strftime("%d/%m/%Y")
	headers = {'Content-type': "application/json"}
	data = {"author": author, "text": text, "product_id": product_id, "date": today}
	requests.post("{}/create_comment".format(api_url), json=data, headers=headers)
	return redirect('/{}'.format(product_id))

# falta la ruta y función para crear un producto, además del form en el html
# también falta la función para filtrar productos por precio
	
if __name__ == '__main__':
	app.run()