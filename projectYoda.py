people = {}

#First function takes a name parameter and adds a new contact to the name-list
def addPerson():
    while True:
        print('Enter name:')
        newName = input()
        if newName == '':
            continue
        print('Enter age:')
        newAge = input()
        if newAge == '':
            pass     

##  people[Name] = Age

#Second function displays the print: "Name is age years old."
def nameAndAge(newName,newAge):
    for newName, newAge in people.items():
        print(key + ' is ' + str(value) + ' years old.')

addPerson()
nameAndAge(newName,newAge)
