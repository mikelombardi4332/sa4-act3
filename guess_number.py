number = 10
incorrect_ans = True
total_guesses = 3
while incorrect_ans:
    print(f"You have {total_guesses} chance(s) left...\n")
    if total_guesses == 0:
        print(f"You are out of chances, the answer was: {number}")
        break
        
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
    else:
        print(f"Sorry! Try again.")
        total_guesses -=1