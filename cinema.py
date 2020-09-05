films={ "Finding Doru":[3,5],
            "Bourne":[12,5],
            "Tarzan":[15,4],
            "Ghost Buster":[12,6]
    }
while True:
    choice=input("Which film you want to watch?: ").strip().title()
    if choice in films:
        age=int(input("How old are you?: ").strip())
        #check user age
        if age>=films[choice][0]:
            #check seats
            if films[choice][1]>0:
                print("Enjoy!!")
                films[choice][1]=films[choice][1]-1
            else:
                print("No more seats available")
        else:
            print("You are too young to watch {}".format(choice)) 
    else:
        print("We don't have that film :(")
    
