from flask import Flask, render_template, request, redirect, url_for
from db import insert_bike,get_all
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',data = get_all())

@app.route('/new_bike')
def new_bike():
    return render_template('new_bike.html')

@app.route('/new_bike',methods=['POST'])
def post_new_bike():
    bike_name = request.form.get('name')
    bike_fee = request.form.get('price')
    bike_image = request.form.get('image')
    bike_year = request.form.get('year')
    insert_bike(bike_name,bike_fee,bike_image,bike_year)
    return redirect(url_for("index"))

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 