known_users=["alice","bob","jack","emily","micheal","rosy","john"]
'''print(known_users)
print(len(known_users))'''
while True:
    print("Hello, Travis here!")
    name=input("Enter you name: ").strip()

    if name in known_users:
        print("Hello {}!".format(name))
        remove=input("Do you want to exit?: ")
        if remove=="y" or remove=="Y":
            known_users.remove(name)
            print(known_users)
        if add=="n" or add=="N":
            print("Happy to have you {}".format(name)) 
    else:
        print("You are not a part of the system {}".format(name))
        add=input("Want to be a part?: ")
        if add=="y" or  add=="Y":
            known_users.append(name)
            print(known_users)
        if add=="n" or add=="N":
            print("No worries, Bye {}".format(name))
