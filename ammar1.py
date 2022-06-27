empty_list = []

while True:
    name_input = input("Insert your name: ")

    if name_input == '':
        break

    empty_list.append(name_input)

dict_name = dict.fromkeys(empty_list)

print("CURRENT LIST WITH NO :",dict_name)

# insert the name that you want to update the age
while True:
    key = input("Insert the name of the person:")
    update_age = input("Insert your Age:")

    # if there is no input, press enter
    # no input means it should break 
    if key == '' and update_age == '':
        break 

    # if theres input, it will update the dict
    else:
        dict_name[key] = update_age

print("UPDATED DICTIONARY:", dict_name)