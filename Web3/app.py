from flask import Flask, render_template, request, redirect, url_for
from db import get_all,insert_food,get_food_by_id,update_food_by_id,delete_food_by_id
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html',data = get_all())

@app.route('/', methods=['POST'])
def add_dish():
    dish_name = request.form.get('name')
    dish_price = int(request.form.get('price'))
    insert_food(dish_name,dish_price)
    return redirect(url_for('index'))

@app.route('/edit_food/<food_id>',methods = ['POST'])
def put_food(food_id):
    dish_name = request.form.get('name')
    dish_price = int(request.form.get('price'))
    update_food_by_id(food_id,dish_name,dish_price)
    return redirect(url_for('index'))
 
@app.route('/edit_food/<food_id>')
def func_name(food_id):
    dish=get_food_by_id(food_id) 
    return render_template('edit_food.html',food = dish)

@app.route('/delete_food/<food_id>')
def delete_food(food_id):    
    delete_food_by_id(food_id)
    return redirect(url_for('index'))
    
if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 