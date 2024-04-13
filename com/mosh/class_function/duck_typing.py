# Duck typing --> if its quack like a duck, walk like a duck, then it is a duck

# where type, class of the object is less important than the method defines.

# Using duck typing, it will do not consider types at all.instead it will consider the presence of given method or attributes
class Dog:
    def speak(self):
        print("woof!")


class Cat:
    pass


def sound(animal):
    animal.speak()


dog = Dog()
cat = Cat()

sound(dog)
sound(cat)
