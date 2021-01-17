from flask import Flask, render_template, request, jsonify
import json, requests

app = Flask(__name__)

@app.route('/comments')
def get_comments():
	with open("comments.json") as json_file:
		comments = json.load(json_file)
		return jsonify(comments)

@app.route('/products')
def get_products():
	with open("products.json") as json_file:
		products = json.load(json_file)
		return jsonify(products)

@app.route('/create_product')
def create_product():
	# products_request = requests.get(url = "http://localhost:5000/products")
	# products = products_request.json()
	# return str(sorted(products, key = lambda i: i["id"], reverse=True)[0]["id"])
	ids["last_product_id"] += 1
	name = request.args.get('name')
	price = int(request.args.get('price'))
	image = request.args.get('image')
	score = []
	new_product = {"id": ids["last_product_id"], "name": name, "price": price, "image": image, "score": score}
	save_ids()
	print("\n\n", new_product, "\n\n")
	with open("products.json", "r") as json_file:
		products = json.load(json_file)
		products.append(new_product)
	with open("products.json", "w") as json_file:
		json.dump(products, json_file)
	return new_product

@app.route('/create_comment')
def create_comment():
	ids["last_comment_id"] += 1
	author = request.args.get('author')
	product_id = int(request.args.get('product_id'))
	text = request.args.get('text')
	date = request.args.get('date')
	new_comment = {"id": ids["last_comment_id"], "author": author, "product_id": product_id, "text": text, "date": date}
	save_ids()
	print("\n\n", new_comment, "\n\n")
	with open("comments.json", "r") as json_file:
		comments = json.load(json_file)
		comments.append(new_comment)
	with open("comments.json", "w") as json_file:
		json.dump(comments, json_file)
	return new_comment

@app.route("/rate_product")
def rate_product():
	product_id = int(request.args.get('product_id'))
	score = int(request.args.get('score'))
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
	

if __name__ == '__main__':
	ids = {}
	ids_file = open("ids.txt")
	for line in ids_file:
		line_list = line.strip().split(',')
		ids[line_list[0]] = int(line_list[1])
	app.run()