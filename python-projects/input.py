num = int(input("enter a number: "))
print(num)

#num += 10 #this code is fine as long as it's cast to an int above
print(num)


try:
    num = int(input("Enter a number: "))
    num+=10
except:
    print("you didnt enter a number")


print("continue")


with open("movies.txt") as file:
    for line in file:
        line = line.strip() #this makes it so when you print there isnt a space in between each
        print(line)


#when reading in the heihgts and use the split function, it gets put into a list as strings. mgiht want to amke the third token an int
        
with open("heights.txt") as file:
    for line in file:
        line = line.strip()
        lst = line.split() #how do i make the third token an int
        print(lst)