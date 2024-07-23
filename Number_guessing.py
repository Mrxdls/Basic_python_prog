import random
import math
lower_range = int(input("Enter Lower range of for the number: "))
upper_range = int(input("Enter Upper range of for the number: "))
random_num = random.randint(lower_range,upper_range)
player_chances = math.ceil(math.log(upper_range-lower_range+1,2))
chances = 0
# result = False
while player_chances > chances:
    print(f"you have {player_chances - chances} chances ")
    chances+=1
    guessing_num = int(input(f"guess the number in range between {lower_range} to {upper_range} :"))
    if guessing_num == random_num:
        print(f"you guess the correct number : {guessing_num}")
        # result = True
        break
    elif guessing_num > random_num:
        print("number is greater then the random number")
    elif guessing_num < random_num:
        print("number is less then the random number")
# if not result:
print(f"the number is {random_num}")
print("better luck next time")