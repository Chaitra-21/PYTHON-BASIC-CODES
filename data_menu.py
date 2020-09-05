# Ask user for name
name=input("What is your name?: ")

#Ask user for age
age=input("What is your age?: ")

#Ask user for city
city=input("What is you city?: ") 

#Ask user what they enjoy
love=input("What do you like?: ")

#Create output
string="You name is {}, you are {} years old, you live in {}, you love {}"
output=string.format(name,age,city,love)
#Print output to screen
print(output)
