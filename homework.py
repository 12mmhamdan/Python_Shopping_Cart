import os
def clear_output():
    os.system("cls" if os.name == "nt" else 'clear')
### Exercise 2 - Write a Python class for an Animal that has a name and energy attributes. The animal class should also have methods for eat, sleep, and play that will take in an integer and increase/decrease the energy of the animal with a formatted print statement
# Example 1
# buddy = Animal('Buddy', 10)
# buddy.play(5) -> "Buddy is playing for 5 minutes. His energy is now 5"
# buddy.sleep(10) -> "Buddy is sleeping for 10 minutes. His energy is now 15"
class Animal():
    def __init__(self, name, energy_level=100):
        self.energy_level = energy_level
        self.name = name
    def play_time(self):
        energy_decrease = int(input(f"How much did {self.name.title()} play?"))
        clear_output()
        self.energy_level = self.energy_level - (energy_decrease)
        if self.energy_level <= 30:
            print(f"{self.name.title()} is almost out of energy! Please feed {self.name.title()} or let {self.name.title()} sleep to get some energy back!")
        else:
            print(f"Hope it was fun!")
    def eat(self):
        energy_increase = int(input(f"How much did {self.name.title()} eat?"))
        clear_output()
        self.energy_level = self.energy_level + (energy_increase)
        if self.energy_level >= 100:
            print(f"{self.name.title()} is full of energy! You should take {self.name.title()} outside to play!")
        elif self.energy_level <=30:
            print(f"{self.name.title()} is really hungry!")
        elif input (f"What did {self.name.title()} eat?"):
            print(f"Awesome! Sounds delicious!")
        else:
            return
    def sleep(self):
        energy_increase = int(input(f"How much did {self.name.title()} sleep?"))
        clear_output()
        self.energy_level = self.energy_level + (energy_increase)
        if self.energy_level <= 0:
            self.energy_level=0
            print(f"{self.name.title()} is all out of energy with {self.energy_level} energy left.\nPlease give {self.name.title()} food or let them sleep to get some more energy back!")
        else:
            print(f"Here is the new energy level for {self.name.title()}\n{self.energy_level}")
animal1 = Animal('bob', 300)
animal2 = Animal('Tom')
animal1.play_time()
animal1.eat()
animal1.sleep()
animal2.play_time()
animal2.eat()
animal2.sleep()
