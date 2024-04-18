from dog import Dog

d1 = Dog("Jillian", "roll", "corgi", True)



#This is how you call the name + breed number, basic string method
print(d1)


#just calling all the functions because didnt have time to read it

print(d1.speak())

print(d1.feed())

print(d1.get_name())

print(d1.get_breed())

print(d1.get_trick())


print(d1.change_trick())

'''
with open('dogs.txt', 'r') as dog_file:
    dog_names = []
    
    for line in dog_file:
        values = line.split()
        #dog_names = []

        
        height_in_inches = int(values[2])
        feet, inches = divmod(height_in_inches, 12)
        print(values[0], values[1], 'is', feet, 'feet,', inches, 'inches tall.')
'''


