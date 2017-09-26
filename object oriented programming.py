# Building objects in python involves creating classes with
# several methods(functions associated with objects) performing different functions
# within the body of the class
import random
#Instantiating a class
class Critter(object):

	total = 0

	def status():
		print "Total number of critters: ", Critter.total

	status = staticmethod(status)

	""" creating a class ( this tripple quoted string is 
		called 'docstring', it tells what the function does)
	string --> intergers """
# By including the "object" parameter you indicate that the class
# created is declared in terms of an object. classes can also be defined in
# terms of initially created classes
 
# creating constructors

	def __init__(self, name, mood,statement):
		self.name = name
		self.__mood = mood
		self.statement = statement
		print "Hi.  i am a new object number ", self.name, "and I am", self.__mood
		Critter.total += 1

# This contains the string that gets printed when the object 
# is printed
	def __str__(self):
		rep = "Critter object\n"
		rep += "name: "+ self.name + "\n"
		
   
	def talk(self,statement):
# every method in a class must have a first parameter called "self"
# this allows the method to refer back to the object
		print "Hi. I am", self.name, "\n"
		return statement
''' a method can be privately or publicly declared.
a private attribute can only be accessed from within the class and is 
preceeded by two underscores i.e __attr. eg the attribute "mood"
above while a public attribute can be accessed
from outside the class. '''



# main
print "Accessing class attribute "
moods = ["happy","sad","perplexed","relaxed"]


count = 0
while count < 25:
	for num in range(25):
		newcrit = Critter(num+1, random.choice(moods),"")
		count += 1

# print Critter.total

crit1 = Critter("boo","happy","")
# crit2 = Critter("bobby")
# crit3 = Critter("zoho")

# Critter.status()

print crit1.talk("what do you have to say")
print "total critters created: ", Critter.total


crit2 =Critter("jenny","")



