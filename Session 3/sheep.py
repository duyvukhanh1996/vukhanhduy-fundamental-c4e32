ship_sizes = [5, 7, 300, 90, 24, 50, 75]
print("Hello my name is Duy and these are my ship sizes")
print(ship_sizes)
print("Now my biggest sheep has size",max(ship_sizes),"let's shear it")
ship_sizes[ship_sizes.index(max(ship_sizes))] = 8
print("After shearing, here is my flock")
print(ship_sizes)
for j in range(4):
    print("MONTH",j+1)  
    for i in range(len(ship_sizes)):
        ship_sizes[i] = ship_sizes[i] + 50
    print("1 month has passed, now here is my flock")
    print(ship_sizes)  
    print("My flock has size in total:",sum(ship_sizes))
    print("i would get",sum(ship_sizes),"* 2$ =",sum(ship_sizes)*2,"$") 
    print("Now my biggest sheep has size",max(ship_sizes),"let's shear it")
    ship_sizes[ship_sizes.index(max(ship_sizes))] = 8
    print("After shearing, here is my flock")
    print(ship_sizes)
    print()
    print()