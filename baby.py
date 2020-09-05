from random import choice
questions=["Why is sky blue: ", "Why sun in morning: ","Why egg oval: "]
question=choice(questions)
answer=input(question).strip()
while answer!="Just because":
    answer=input("why?: ").strip()
print("Oh...okay")
