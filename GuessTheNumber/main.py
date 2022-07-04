import random

max_range = input("From 1 to what number range you want to guess? Enter the number: ")
userNumber = input("Enter your number: ")

randomNumber = random.randrange(0,int(max_range))

while(userNumber != randomNumber):
    if int(userNumber) > randomNumber:
        print("Ups, its not this number, try again!")
        print("Hint: number is smaller than your type!")
    if randomNumber > int(userNumber):
        print("Ups, its not this number, try again!")
        print("Hint: number is higher than your type!")
    if randomNumber == int(userNumber):
        print("Congratulation, your answer is good!")
        another_round = input("Are you ready for another round? Yes? Type y and press Enter!")
        if another_round == "y" or another_round == "Y":
            max_range_choose = input("You wanna change random range? Your last choose was from 1 to " + max_range +
                              ". Type y if you want to change range from 0 to your choose!")
            if max_range_choose == "Y" or max_range_choose == "y":
                max_range = input("Type your new range!: ")

            randomNumber = random.randrange(0,int(max_range))
        else:
            break

    userNumber = input("Enter your number: ")

print("Thank you! Bye!")

