class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old")
        return self

a_person = Person("Sal", 29)
# a_person.greeting()


class Superhero(Person):
    def __init__(self, superhero_name, superhero_power, secret_identity, age):
        super().__init__( superhero_name, age)
        self.superhero_power = superhero_power
        self.secret_identity = secret_identity

    def greeting(self):
        print(f"Hi, I am {self.name}")


spider_man = Superhero("Spider-Man", "Webs", "Peter Parker", 15)
# spider_man.greeting()

my_list = [a_person, spider_man] 
for item in my_list:
    # item = a_person
    # item = spider_man
    item.greeting()