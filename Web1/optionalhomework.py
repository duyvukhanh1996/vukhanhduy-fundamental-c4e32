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
maxx =n-1
minn = 0


# Lặp dần vào trong
while count <= n**2:
    # Vẽ dòng trên
    for i in range (minn,maxx):
        A[minn][i] = count
        count += 1

    # Vẽ dòng phải
    for i in range (minn,maxx):
        A[i][maxx] = count
        count += 1

    # Vẽ dòng dưới
    for i in range (maxx,minn,-1):
        A[maxx][i] = count
        count += 1

    # Vẽ dòng trái
    for i in range (maxx,minn,-1):
        A[i][minn] = count
        count += 1


    minn += 1
    maxx -= 1 
    #Nếu N lẻ bị lặp vô hạn nên cần gán phần tử ở giữa rồi break
    if count == n**2:
        A[maxx][maxx] = n**2
        break

# In kết quả
for i in range(n):
    for j in range(n):
        if A[i][j] < 10:
            print(A[i][j],end = "  ")
        else:
            print(A[i][j],end = " ")
    print()

    








