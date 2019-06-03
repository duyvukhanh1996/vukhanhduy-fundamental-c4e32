connections = [
    ["A","B"],
    ["A","D"],
    ["B","A"],
    ["B","E"],
    ["B","G"],
    ["C","D"],
    ["C","G"],
    ["D","A"],
    ["D","E"],
    ["D","C"],
    ["E","B"],
    ["E","D"],
    ["E","H"],
    ["G","C"],
    ["G","B"],
    ["H","E"]
]
start = "A"
stop = None
result = []

while stop != "H":
    for i in connections:
        if i[0] == start:
            stop == i[1]
            start == i[1]
            result.append(i)







