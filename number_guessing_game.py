import random 

max_number = input("Type a number: ")

if max_number.isdigit():
    max_number = int(max_number)
    if max_number <= 0:
        print("Please next time type a number larger than 0!")
        quit()
else:
    print("Please next enter a valid number")
    quit()

random_num = random.randint(0, max_number)
guess_counter = 0
lives = 6

while True:
    if lives == 0:
        print("Game over good luck next time :)")
        break
 
    print(f"You have {lives} lives remaining.")
    
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please next enter a valid number")
        continue
        
    if user_guess == random_num:
        print("Yay! You got it right")
        print("You got it right after", guess_counter, "times")
        break
    elif user_guess > random_num:
        print("The number you choose is way too high.")
        lives -= 1
        guess_counter += 1
    else:
        print("The number you choose is way too low.")
        lives -= 1
        guess_counter += 1
        


