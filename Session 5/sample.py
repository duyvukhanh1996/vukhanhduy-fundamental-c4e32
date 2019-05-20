def tinh_toan(a,b,o):
    if o == "+":
        return a + b
    if o == "-":
        return a - b
    if o == "*":
        return a * b
    if o == "/":
        return a / b

x = tinh_toan(2,3,"/")
print(x)