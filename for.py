'''for i in range(1,21):
    print(i)
for i in  "chaitra":
    print(i)
for i in range (1,50,3):
    print(i+1)'''
vowels=0
consonants=0

for letter in "Hello":
    if letter in "aeiou":
        vowels=vowels+1
    elif letter==" ":
        pass
    else:
        consonants=consonants+1
print("There are {} vowels".format(vowels))
print("There are {} consonants".format(consonants))
