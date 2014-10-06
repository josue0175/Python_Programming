#define objects
#2. create class
#3. object is instance is a class
#4. not camel case

#1.) introduce simple class and logic with methods
class pet:
    number_of_legs = 0
    
    def sleep(self): #must always include "self" first in the list
        print "zzz"

    def count_legs(self): #must always include "self" first in the list
        print "I have %s legs." % self.number_of_legs

#Inheritance
class dog(pet):
    def bark(self):
        print "woof"
       
doug = pet()
doug.number_of_legs = 9
doug.count_legs()
nemo = pet()
nemo.number_of_legs = 1
nemo.count_legs()
doug.sleep() #will add argument by itslef

#inheritance
#Belongs to pet and dog classes
doug = dog()
doug.bark()
doug.sleep()
doug.number_of_legs = 4
doug.count_legs()
