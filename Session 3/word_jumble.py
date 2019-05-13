from random import choice 
list_word = ["meticulous","champion","hexagon"]
word = choice(list_word)
chars = list(word)
new_chars = []
x = ""
playing = True

for i in range(len(chars)):
    x = choice(chars)
    chars.remove(x)
    new_chars.append(x)
print(*new_chars)

while playing:
    answer = input("Your answer: ")
    answer = answer.lower()
    if answer != word:
        print(":(")
    else:
        print("Hura")
        playing = False