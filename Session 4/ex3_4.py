Questions = [
    {
    "Intro" : "Answer the following algebra question:",
    "Question" : "If x = 8, then what is the value of 4(x+3) ?",
    "Answer" : [35,36,40,44],
    "Correct" : "4"
    },
    {
    "Intro" : "Estimate this answer (exact calculation not needed):",
    "Question" : "Jack scored these marks in 5 math tests: 49, 81, 72, 66 and 52. What is the mean?",
    "Answer" : ["About 55","About 65","About 75","About 85"],
    "Correct" : "2"
    }
]
correctly_answer = 0
for question in Questions:
    print(question["Intro"])
    print(question["Question"])
    for i in question["Answer"]:
        print(question["Answer"].index(i)+1,". ",i)
    while True:
        YourAnswer = input("Your Choice (1,2,3,4):")
        if YourAnswer in ["1","2","3","4"]:
            break
    if YourAnswer == question["Correct"]:
        print("Bingo")
        correctly_answer += 1
    else:
        print(':(')
print("You correctly answer",correctly_answer,"out of",len(Questions),"questions")