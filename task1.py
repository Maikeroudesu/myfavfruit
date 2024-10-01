myfavfruitsnum = int(input("Enter number of your fave fruit: "))

myfavfruits=[]

for i in range(myfavfruitsnum):
    fruits = input ("Enter fruits:")
    myfavfruits.append(fruits)

print(myfavfruits)

for data in myfavfruits:
    if data == "banana":
        break
    elif data == "apple":
        print ("happy eating")
