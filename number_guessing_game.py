import random

lower_bound = int(input("Enter lower bound: "))
upper_bound = int(input("Enter upper bound: "))

chances = 7

if(lower_bound < upper_bound):
    random_number = random.randint(lower_bound, upper_bound)
    for i in range(chances):

        try:
            guess_number = int(input("Guess the number: "))
        except ValueError:
            print("Invalid input! Please enter an integer.")
            continue

        if (guess_number < random_number):
            print("Too low! Try again.")
        
        elif (guess_number > random_number):
            print("Too high! Try again.")
        
        else: 
            print("Congratulations! You guessed the number.")
            print(f"The number was {random_number}, and you guessed it in {i + 1} chances.")
            break
        
        print(f"Wrong! {chances - i - 1} chances left.") 
    
    else:
        print(f"Game over! The number was {random_number}.")

else:
    print("Lower bound should be less than upper bound")