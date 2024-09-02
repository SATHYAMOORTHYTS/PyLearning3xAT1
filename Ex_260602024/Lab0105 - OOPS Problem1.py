class Dog:
    # Attributes

    name = None # None - Default value
    breed = None
    age = None
    color = None

    #  Behaviour
    def sleep(self):
        print("zzz Sleeping")
    def eat(self):
        print("Eating")

dog1 = Dog() # Object creation
dog1.eat()
dog2 = Dog() # Object creation
dog2.sleep()
