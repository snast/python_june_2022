def add(a,b,c=0):	# function name: 'add', parameters: a and b
    x = a + b	# process
    return x	# return value: x

add(3,7)
# Function that gives a welcome message, "Welcome!"
def greeting():
    x = "Welcome!!"
    print(x)

greeting()

# two parameters, phrase, num of times we want to repeat it
# "Welcome Sal", 3
# Welcome Sal
# Welcome Sal
# Welcome Sal
# repeat_phrase("Welcome Sal", 3)


def repeat_phrase(phrase="Welcome Sal", times_to_repeat=2):
    # print(phrase* times_to_repeat)
    print("Testing sal's function")
    for i in range(times_to_repeat):
        print(i)
        print(phrase)
    print("Finished sal's function")
    
repeat_phrase("Welcome Sal", 3)
repeat_phrase()
repeat_phrase("I Love Python")
repeat_phrase(5)
repeat_phrase(times_to_repeat=5)
repeat_phrase(phrase="Hello World")
print(repeat_phrase(times_to_repeat=10, phrase="Summer is here!"))
print(add(1,2))
sum = add(1,2)
print(sum)

def number_list(number):
    my_list = []
    for i in range(number):
        my_list.append(i)
    return my_list

def is_happy(happiness_score):
    if happiness_score >=70:
        return True
    else:
        return False

student = {'name': 'Sal', 'happiness_score': 69}
if is_happy(student['happiness_score']):
    print(f"{student['name']} is happy!")
else:
    print(f'{student["name"]} is feeling a bit down today!')

my_new_number_list = number_list(10)
# if we omit the return statement(line 46) my_num_number_list - > NONE
print(my_new_number_list[3])
# FLASK
# getAll() - > list of all users -> [u1, u2, u3]
