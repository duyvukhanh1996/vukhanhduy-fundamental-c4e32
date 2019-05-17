import string
alphabet_list = list(string.ascii_lowercase)
alphabet = {}
for i in alphabet_list:
    alphabet[i] = 0

print(*alphabet)

string = input("Enter your string:").lower()

for key in alphabet:
    alphabet[key] = string.count(key)


for key,item in alphabet.items():
    if item != 0:
        print(key,'    ',item)

