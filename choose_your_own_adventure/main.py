name = input("type your name: ")
print("welcome", name, "to this adventure!")

answer = input("you are on a dirt road it has come to an end"
               " you can go Left or RIGHT. which way would you like to go?")

if answer == "left":
    answer = input("you come to a river, you can WALK around it or SWIM accross it? ")

    if answer == "swim":
        print("you swam across and were eaten by an allagator. ")
    elif answer == "walk":
        print(" you walked for many miles you walked for many miles ran out of water and lost the game.")
    else:
        print("not a valid option. you lose.")

elif answer == "right":
    anwser = input("you come to a bridge it looks wobbly do you want to CROSS it or head BACK ")
    if answer == "cross":
        anwser = input("you cross the bridge and meet a stranger do you talk to them (YES/NO)")
        if answer == "yes":
            print("you talk to the stranger and they give you gold you win!")
        elif answer == "no":
            print("you ignore the stranger and they are offended and you lose.")
        else:
            print("not a valid option. you lose.")
    elif answer == "back":
        print("you go back and lose ")
    else:
        print("not a valid option. you lose.")
else:
    print("not a valid option. you lose.")

print("thanky you for trying" ,name)
