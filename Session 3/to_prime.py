n = int(input("Nhap N:"))
while not 0 < n < 1000000:
    n = int(input("Nhap lai N > 0 va N < 10000:"))

a = n
list_prime = []
while a != 1:
    for i in range(2,n):  #????
        if a % i == 0:
            list_prime.append(i)
            a = a/i
            break
print(n,"=",end=" ")
print(*list_prime,sep="*")