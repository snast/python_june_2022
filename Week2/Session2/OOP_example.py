class CoffeeM:
    def __init__(self,name):
        self.name = name
        self.water_temp = 200
    def brew_now(self,beans):
        print(f"Using {beans}!")
        print("Brew now brown cow!")
    def clean(self):
        print("Cleaning!")

class CappuccinoM( CoffeeM ):
    def __init__(self,name):
        super().__init__(name)
        self.milk = "whole"
    def make_cappuccino(self,beans):
        super().brew_now(beans)
        print("Frothy!!!")
        return self
    def clean(self):
        super().clean()
        print("Cleaning the frothy stuff!")

normal_coffee = CoffeeM("Americano")
normal_coffee.brew_now("Java").clean()

cappuccino = CappuccinoM("Cappuccino")
cappuccino.make_cappuccino("Java")
cappuccino.clean()

