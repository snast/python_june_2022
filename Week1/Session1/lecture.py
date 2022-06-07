# var return_string="return String";
# return_string = "returnString"
# print(return_string)
# new_number = 23
# def sals_method():
#     print("Welcome to sal's method")
# sals_method()

# if(new_number == 23):
#     print("New number is 23")
# else:
#     print("Number did not match")

# # Integers
# price = 20
# another_price = 10
# total_price = price + another_price
# print(total_price)
# print(50)
# message = "My age is"
# sals_age = 29
# print(message + str(sals_age))
# # Strings
# first_name = "Sal"
# last_name = "The Instructor"
# full_name = first_name + last_name
# print(full_name)
# # Booleans
# is_valid = True
# is_hungry = False
# if is_hungry:
#     print("I am hungry")
# else:
#     print("I'm full")
# float_price = 99.99


# Lists - 0 based indexing
colors = []
blue = "Blue"
red = "Red"
green = "Green"
print(colors)
colors.append(blue)
print(colors)
colors.append(red)
print(colors)
colors.append(green)
print(colors)
print(len(colors))
print(colors[0])
# Dictionaries - Key/Value
my_dict = {
    "name": "Sal The Instructor",
    "age": 29,
    "stack": "Python"
}
my_dict['name'] = 'Sal Abd Salim Nast'
print(my_dict['name'])


print(my_dict['age'])
my_dict["location"] = "Seattle"
print(my_dict)
# Tuples
dog = ("Canis Familiaris", "dog", "carnivore", 12)
#Unable to run code, because tuples are immutable
# dog[3] = 15

#Conditionals
is_hungry = True
age=29
if is_hungry:
    print("I am hungry")
    if(age > 18):
        print("you are 18")
elif is_hungry == True:
    print("I'm full")

#loops
# colors = ['blue', 'red', green']
for silly_color in colors:
    print(silly_color)

# range(3) = [0,1,2]
for index in range(3):
    print(colors[index])