# Create three dictionaries to represent three students. 
# Each dictionary should have the name(String), age(Integer), email(String) for each student.
# Put the three students in a list.  Use a for loop to print out the information for each student.

#mylist[0]
# my_list = [a, b, c]
#my_dict['key'] = {"key": "value"}
mylist = [
    {"name":'Charlie', "age":30, 'email': 'charlie@gmail.com'}, 
    {"name":'Stephen', "age":31, 'email': 'stephen@gmail.com'} , 
    {"name":'Alex', "age":27, 'email': 'alex@gmail.com'},
]

for item in mylist:
    # sal = {"name":'Charlie', "age":30, 'email': 'charlie@gmail.com'}
    print(f"Our students's names: {item['name']}")
    print(f"Our students's ages: {item['age']}")
    print(f"Our students's emails: {item['email']}")

age = 29
name = "Sal"
welcome_statement = f"My name is {name}"
# my_dict = {
#     "list1": [2,3,4],
#     "list2": ['sal', 'kyle']
# }


