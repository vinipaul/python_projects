from flask import Flask,jsonify,request,json
app=Flask(__name__)
@app.route('/',methods=['GET'])
def show_hello():
    return "hello"
@app.route('/products',methods=['GET'])
def show_products():
    data=product_details_from_jsonfile()
    return jsonify(data)
def product_details_from_jsonfile():
    with open('products.json','r',encoding="utf-8") as file:
     return json.load(file)
def save_product_details(new_product):
    with open('products.json','w') as file:
       json.dump(new_product,file,indent=4)
@app.route('/products/<int:product_id>',methods=['GET'])
def show_product_by_id(product_id):
    product_list=product_details_from_jsonfile()
    required_product=None
    for p in product_list:
        if p["id"]==product_id:
            required_product=p
            break
    if required_product!=None:
        return jsonify(required_product)
    else:
        return "not found error 404"
@app.route('/products',methods=['POST'])
def add_products():
    new_product_details=request.json
    product_list=product_details_from_jsonfile()
    product_list.append(new_product_details)
    save_product_details(product_list)
    return new_product_details
@app.route('/products/<int:product_id>',methods=['PUT'])
def update_product_details(product_id):
    update_details=request.json
    required_id_product=None
    product_list=product_details_from_jsonfile()
    for p in product_list:
        if p["id"]==product_id:
            required_id_product=p
            break
    required_id_product.update(update_details)
    save_product_details(product_list)
    return update_details       
@app.route('/products/<int:product_id>',methods=['DELETE'])
def delete_a_product(product_id):
    product_list=product_details_from_jsonfile()
    for p in product_list:
        if p["id"]==product_id:
            deleted_product=p
            break
    product_list.remove(deleted_product)
    save_product_details(product_list)
    return deleted_product
app.run(debug=True)