from flask import Flask, render_template, request
app = Flask(__name__)

data = [
  {"username":"duyvukhanh","password":"123456"},
  {"username":"duyvukhanh1996","password":"123456789"}
]
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods = ["POST"])
def login():
    login = False
    username = request.form.get('username')
    password = request.form.get('password')
    for item in data:
      if username == item['username'] and password == item['password']:
        login = True
        break
    return render_template('login.html',login = login)


if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 