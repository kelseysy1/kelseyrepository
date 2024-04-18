from student import Student

s1 = Student("Jillian", "Demerlier", 420)


#This is how you call the name + id number, basic string method
print(s1)

#This is how you call the greeting function
print(s1.greeting())

#call the take exam function
print(s1.take_exam())

#and again
print(s1.take_exam())

#get the energy level :D
print(s1.get_energy_level())