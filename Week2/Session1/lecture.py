import random
class User:
    dojo = "Coding Dojo"
    # Instance Method
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.stack = "Python"
        self.email = email

    #return a string representing the full name
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    #increase age of user by 1
    def birthday(self):
        self.age += 1
        return self

    #instance method to print out greeting Hello, my name is Sal Nast
    def greeting(self):
        print(f"Hello, my name is {self.full_name()}!")

    # Class Method
    @classmethod
    def get_bob_the_user(cls):
        return User("Bob", "The Builder", 35, "bobthebuilder@codingdojo.com")

    @classmethod
    def get_random_user(cls):
        list_of_names = ["alice", "bob", "charlie"]
        return User(list_of_names[random.randint(0,3)], "Johnson", random.randint(13,100), "AliceJohnson@codingdojo.com")


my_user = User("Sal", "Nast", 29, "snast@codingdojo.com")
print(my_user.full_name())
my_user.birthday().birthday().birthday().birthday().birthday()
# my_user.birthday() - > my_user.birthday().birthday().birthday().birthday()
print(my_user.age)
print(my_user.greeting())
another_user = User("Kyle", "Reimers", 29, "kreimers@codingdojo.com")
print(another_user.full_name())
print(another_user.age)

print(my_user.dojo)
print(User.dojo)

bob_user = User.get_bob_the_user()
print(bob_user.full_name())
random_user = User.get_random_user()
print(random_user.age)
print(random_user.first_name)