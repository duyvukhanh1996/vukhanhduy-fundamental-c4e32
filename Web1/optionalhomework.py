# Nhập N
n = int(input('N:'))

#Tạo ma trận NxN
A=[]
for i in range(n):
    A.append([])
for j in range(n):
    for i in range(n):
        A[j].append(0)

# gán các giá trị ban đầu
count = 1
max_row =n-1
max_col =n-1
min_row=0
min_col=0

# Lặp dần vào trong
while count <= n**2:
    # Vẽ dòng trên
    for i in range (min_row,max_row):
        A[min_row][i] = count
        count += 1

    # Vẽ dòng phải
    for i in range (min_row,max_row):
        A[i][max_col] = count
        count += 1

    # Vẽ dòng dưới
    for i in range (max_row,min_row,-1):
        A[max_row][i] = count
        count += 1

    # Vẽ dòng trái
    for i in range (max_col,min_col,-1):
        A[i][min_col] = count
        count += 1


    min_col += 1
    min_row += 1
    max_col -= 1
    max_row -= 1

    #Nếu N lẻ bị lặp vô hạn nên cần gán phần tử ở giữa rồi break
    if count == n**2:
        A[max_row][max_col] = n**2
        break

# In kết quả
for i in range(n):
    for j in range(n):
        if A[i][j] < 10:
            print(A[i][j],end = "  ")
        else:
            print(A[i][j],end = " ")
    print()

    








