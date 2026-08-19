#Number Guess Game :->
num=7
guess=0
while num!=guess:
    guess=int(input("Enter your guess:"))
    if guess==num:
        print("congratulation's")
        break
    else:
        print("try again")
    choice=input("Do You Whant TO Continu Pls Enter (y/n)").lower()
    if choice=="y":
        continue
    else:
        print(Exiting)
        break
