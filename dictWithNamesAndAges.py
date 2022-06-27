# This function is to know the basic of printing a dictionary with keys and values. 

nameAndAge = {'Ayuni': 38, 'Nadia': 37, 'Izura':31}
def displayNameAndAge(nameAndAge):
    for k,v in nameAndAge.items():
        print(k + ' ' + str(v))
    print()
displayNameAndAge(nameAndAge)