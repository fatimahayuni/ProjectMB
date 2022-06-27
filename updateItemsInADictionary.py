userDict={}
counter=1
while True:
    name = input("enter name: ")
    age = input("enter age: ")
    userDict[(name,age)]=counter
    choice = input("do you want to continue y:yes/press any other key to quit: ")
    if choice=="y" or choice=="Y":
        break
