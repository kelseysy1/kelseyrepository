from car import Car


c1 = Car("blue", "4_cylinder", 100, 0)

c2 = Car("green", "V8", 100, 0)

#List to store the car objects? I'm so dumb it literally said to do this in the instructions lol.
cars = []

with open('cars.txt', 'r') as file:
    for line in file:
        values = line.split()
        color = values[0]
        engine = values[1]
        gas = int(values[2]) #convert to int!
        odom = int(values[3]) 


        #create a new Car object and append it to the cars list
        car = Car(color, engine, gas, odom)
        cars.append(car)
        #now have five car objects stored in the list 'cars'
        #access individual car objects by indexing the 'cars'list
        # ex. cars[0] gives you the first car object

#prints the debugging __str__ function
print(c1)
print(c2)
print(cars[0])


#don't forget to actually call the function lol
print(c1.drive())

print(c2.drive())

print(cars[0].drive()) #ICONIC


print(c1.get_gas_tank())
print(c2.get_gas_tank())

print(c1.get_odometer())
print(c2.get_odometer())