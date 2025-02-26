import random as rn 

print("welcome to the game!\ni will guess a number from 0-100\n\nchose your difficulty\n1. easy - 10 chances\n2. medium - 5 chances\n3. hard - 3 chances")

while True:
    num = rn.randint(0 , 100)


    difficulty = input("-> ")

    if difficulty == "1":
        for i in range(10):
            ans = input("enter your guess -> ")

        if ans < num:
            print("wrong one! the number is greater than", ans)

        elif ans > num:
            print("wrong one! the number is less than", ans)

        else:
            print("HOORAY! you did it!")
            break
    else:
        print("the number was", num)


    if difficulty == "2":
        for i in range(5):
            ans = input("enter your guess -> ")

        if ans < num:
            print("wrong one! the number is greater than", ans)

        elif ans > num:
            print("wrong one! the number is less than", ans)

        else:
            print("HOORAY! you did it!")
            break
    else:
        print("the number was", num)


    if difficulty == "3":
        for i in range(3):
            ans = input("enter your guess -> ")

        if ans < num:
            print("wrong one! the number is greater than", ans)

        elif ans > num:
            print("wrong one! the number is less than", ans)

        else:
            print("HOORAY! you did it!")
            break
    else:
        print("the number was", num)

    
    print("do you want to play again? (y/n)")
    play_again = input("-> ")
    if play_again == "y":
        continue
    else:
        break
