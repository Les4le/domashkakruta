class Budilnik:
    def __init__(self, time):
        self.time = time

    def set_time(self, new_time):
        self.time = new_time

    def get_time(self):
        return self.time

    def pikat(self):
        print(f"pikayu {self.time}!")
        
class Cat:
    def __init__(self, name):
        self.name = name

    def meow(self):
        print(f"meow")
        
object1 = Budilnik("07:00")
objectcat = Cat("Whiskers")
object1.pikat()
objectcat.meow()