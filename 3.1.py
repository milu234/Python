
#class method.
class Car:
    def __init__(self, components):
        self.components = components

    def __repr__(self):
        return f'Car({self.components!r})'

    @classmethod
    def sedan(cls):
        return cls(['suzuki','duccatti'])

    @classmethod
    def tclass(cls):
        return cls(['Maruti','Hyundai'])

print(Car.sedan())
print(Car.tclass())
#staticmethod
import math

class Pizza:
    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients

    def __repr__(self):
        return (f'Pizza({self.radius!r}, '
                f'{self.ingredients!r})')

    def area(self):
        return self.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi


p = Pizza(4, ['mozzarella', 'tomatoes'])
print(p.area())
print(Pizza.circle_area(45))

#innner class
class Human:

 def __init__(self):
    self.name = 'Milan'
    self.head = self.Head()

 class Head:
    def talk(self):
        return 'talking...'

if __name__ == '__main__':
    guido = Human()
    print (guido.name)
    print (guido.head.talk())


#Class Variables

class Shark:
    animal_type = "fish"
    location = "ocean"
    followers = 5

new_shark = Shark()
print(new_shark.animal_type)
print(new_shark.location)
print(new_shark.followers)



#Instance Variables
class Shark:
    def __init__(self,name,age):
        self.name = name
        self.age = age

new_shark = Shark("Milan",6)
print(new_shark.name)
print(new_shark.age)
