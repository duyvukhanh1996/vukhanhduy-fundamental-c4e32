from flask import Flask, render_template
app = Flask(__name__)


# ex1 : without render_template
@app.route('/bmi/<int:weight>/<int:height>')
def bmii(weight,height):
    result = ""
    bmi = weight/((height/100)**2)
    if bmi < 16:
        result = "Your BMI:" + str(bmi) + " | Severely underweight"
    elif 16 <= bmi < 18.5:
        result = "Your BMI:"+str(bmi)+" | Underweight"
    elif 18.5 <= bmi < 25:
        result = "Your BMI:"+str(bmi)+" | Normal"
    elif 25 <= bmi < 30:
        result = "Your BMI:"+str(bmi)+" | Overweight"
    else:
        result = "Your BMI:"+str(bmi)+" | Obese"
    return result

# # ex1 : with render_template
# @app.route('/bmi/<int:weight>/<int:height>')
# def bmii(weight,height):
#     result = ""
#     bmi = weight/((height/100)**2)
#     if bmi < 16:
#         result = "Severely underweight"
#     elif 16 <= bmi < 18.5:
#         result = "Underweight"
#     elif 18.5 <= bmi < 25: 
#         result = "Normal"
#     elif 25 <= bmi < 30:
#         result = "Overweight"
#     else:
#         result = "Obese"
#     return render_template("ex1.html",bmi = bmi,result = result)

@app.route('/user/<username>')
def xxx(username):
    users = {
        "khanh" : {
            "name" : "Nguyễn Khánh",
            "age" : 20,
            "hobbies" : "Chơi púp pê"
        },
        "ahoa" : {
            "name" : "Nguyễn Bá Hoà",
            "age" : 30,
            "hobbies" : "Code"
        },
        "duy" : {
            "name" : "Vũ Khánh Duy",
            "age" : 23,
            "hobbies" : "If you know what i mean"
        }
    }
    return render_template("ex2.html",users=users,username = username)

if __name__ == '__main__':
  app.run(debug=True)