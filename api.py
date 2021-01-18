from flask import Flask, request, jsonify
import json, requests

app = Flask(__name__)

@app.route('/products/<product_id>/comments', methods = ["GET"])
def get_comments(product_id=None):
	with open("comments.json") as json_file:
		comments = json.load(json_file)
	product_comments = []
	for comment in comments:
		if comment["product_id"] == int(product_id):
			product_comments.append(comment)
	return jsonify(product_comments)

@app.route('/products', methods = ["GET"])
def get_products():
	with open("products.json") as json_file:
		products = json.load(json_file)
		return jsonify(products)

@app.route('/products/<product_id>', methods = ["GET"])
def get_product(product_id=None):
	with open("products.json") as json_file:
		products = json.load(json_file)
	for product in products:
		if product["id"] == int(product_id):
			break
	product["mean_score"] = round(sum(product["score"]) / len(product["score"]), 1)
	product["score_amount"] = len(product["score"])
	return jsonify(product)

@app.route('/create_product', methods = ["POST"])
def create_product():
	ids["last_product_id"] += 1
	# cambiar esto
	request_data = request.get_json()
	name = request_data['name']
	price = request_data['price']
	image = request_data['image']
	score = []
	new_product = {"id": ids["last_product_id"], "name": name, 
		"price": price, "image": image, "score": score}
	save_ids()
	print("\n\n", new_product, "\n\n")
	with open("products.json", "r") as json_file:
		products = json.load(json_file)
		products.append(new_product)
	with open("products.json", "w") as json_file:
		json.dump(products, json_file)
	return new_product

@app.route('/create_comment', methods = ["POST"])
def create_comment():
	ids["last_comment_id"] += 1
	request_data = request.get_json()
	author = request_data['author']
	product_id = request_data['product_id']
	text = request_data['text']
	date = request_data['date']
	new_comment = {"id": ids["last_comment_id"],  "product_id": product_id, 
		"author": author, "text": text, "date": date}
	save_ids()
	print("\n\n", new_comment, "\n\n")
	with open("comments.json", "r") as json_file:
		comments = json.load(json_file)
		comments.append(new_comment)
	with open("comments.json", "w") as json_file:
		json.dump(comments, json_file)
	return new_comment

@app.route("/rate_product", methods = ["POST"])
def rate_product():
	request_data = request.get_json()
	product_id = request_data["product_id"]
	score = request_data["score"]
	with open("products.json", "r") as json_file:
		products = json.load(json_file)
		product_to_rate = next(c for c in products if c["id"] == product_id)
		product_to_rate["score"].append(score)
	with open("products.json", "w") as json_file:
		json.dump(products, json_file)
	return product_to_rate

def save_ids():
	ids_file = open("ids.txt", "w")
	for id in ids:
		ids_file.write(id + "," + str(ids[id]) + "\n")
	
def get_ids():
	ids_file = open("ids.txt")
	for line in ids_file:
		line_list = line.strip().split(',')
		if len(line_list) == 2:
			ids[line_list[0]] = int(line_list[1])

if __name__ == '__main__':
	ids = {}
	get_ids()
	app.run()
	# app.run(port=8080)