transcript = [
    {'name':'Nguyễn Văn A','age':'21','address':'Hà Nội','math':7,'physics':8,'chemistry':9,'phone':['01234','23232']},
    {'name':'Vũ Văn B','age':'22','address':'TP HCM','math':6,'physics':8,'chemistry':7,'phone':['62718']},
    {'name':'Lê Văn C','age':'20','address':'Đà Nẵng','math':10,'physics':8,'chemistry':9,'phone':['51287']},
    {'name':'Phạm Văn D','age':'21','address':'Lào Cai','math':9,'physics':7,'chemistry':8,'phone':['06783','51512']},
    {'name':'Đỗ Văn E','age':'22','address':'Quảng Ninh','math':10,'physics':9,'chemistry':8,'phone':['34219','86361']}
]

for student in transcript:
    print("Điểm trung bình của",student["name"],"là",(student["math"]+student["physics"]+student["chemistry"])/3)
print("* "*20)
# --------------------------------------------------------
name_list = []
score_list = []
max_math_name_list = []
for student in transcript:
    name_list.append(student["name"])
    score_list.append(student["math"])
max_score = max(score_list)
for student in transcript:
    if student["math"] == max_score:
        max_math_name_list.append(student["name"])
if len(max_math_name_list) == 1:
    print(*max_math_name_list,"Co diem toan cao nhat la",max_score)
else:
    print(*max_math_name_list,sep=", ",end=" ")
    print("có điểm toán cao nhất là",max_score)
print("* "*20)
# --------------------------------------------------------
phone_number = input("Nhập sđt:")
phone_name = 0
for student in transcript:
    if phone_number in student["phone"]:
        phone_name = student["name"]
if phone_name == 0:
    print("Không ai có sđt này")
else:
    print("Số điện thoại",phone_number,"là của",phone_name)
    










       
    

    
