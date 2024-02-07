number = 10
incorrect_ans = True

while incorrect_ans:
    print("I'm thinking of a number...\n")
    guess = input("What number am I thinking of? (Enter q to quit) ")
    if guess == "q":
        incorrect_ans = False
        print(f"The correct answer is: {number}")
        break
    guess = int(guess)
    
    if guess == number:
        print("Congratulations! You guessed the right number.")
        break
    elif guess > number:
        print("Your guess was too high.\n")
    elif guess < number:
        print("Your guess is too low.\n") 
    else:
        print(f"Sorry! Try again.\n")