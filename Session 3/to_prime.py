list_prime = []

n = int(input("Nhap N:"))
a = n
i = 2

while a != 1:  
    if a % i == 0:
        list_prime.append(i)
        a = a/i
    else:
        i += 1

   
print(n,"=",end=" ")
print(*list_prime,sep="*")