# ----- Basic While Loop -----

print("--- Basic While Loop ---")

count = 0
while count < 5:
    print(f"Count is: {count}")
    count += 1  # Increment count to avoid infinite loop
print("Finished counting to 5!")

# ----- While Loop with 'break' -----

print("\n--- While Loop with 'break' (Secret Number Game) ---")

import random
secret_number = random.randint(1, 10)  # Generate a random secret number between 1 and 10
attempts = 0
max_attempts = 3

print("Guess the secret number between 1 and 10. You have {max_attempts} attempts.")
while attempts < max_attempts:
    try:
        user_guess = int(input(f"Attempt {attempts + 1}: Enter your guess: "))
    except ValueError:
        print("Invalid input! Please enter a whole number.")
        continue  # Skip to the next iteration if input is invalid
    attempts += 1 # Increment attempts

    if user_guess == secret_number:
        print("Congratulations! You guessed it!")
        break # Exit the loop if guessed correctly
    elif attempts == max_attempts:
        print(f"Sorry, you ran out of attempts. The secret number was {secret_number}.")
    else:
        print("Wrong guess! Try again.")
else:
    if attempts == max_attempts and user_guess != secret_number:
        print("Better luck next time!")


# ----- While Loop with 'continue' -----

print("\n--- While Loop with 'continue' (Skipping Even Numbers) ---")

number = 0
while number < 10:
    number += 1
    if number % 2 == 0:
        continue
    print(f"Odd number: {number}")

# --- Infinite loop example (DO NOT RUN FOR LONG!) ---
# This demonstrates what happens if you forget to update the condition
# You can uncomment, run, and then use Ctrl+C in the terminal to stop it.
# while True:
#     print("This will print forever unless stopped!")
#     # No condition update or break here



# ----- Practice Exercise -----

print("\n--- Practice Exercise ---")

print(''' Exercise 1: Countdown: Write a while loop that prints numbers from 10 down to 1, and then prints "Liftoff!".''')

countdown_time = 10
while countdown_time > 0:
    print(countdown_time)
    countdown_time -= 1  # Decrement the countdown
print("Liftoff!")

print(''' Exercise 2: Password Retries: Simulate a simple password retry mechanism.
Define a correct_password = "mysecret".
Initialize attempts_left = 3.
Use a while loop that continues as long as attempts_left > 0.
Inside the loop, prompt the user (using input()) to "Enter password: ".
If the entered password matches correct_password, print "Access granted!" and break the loop.
If not, print "Incorrect password. Attempts left: [remaining attempts]". Decrement attempts_left.
After the loop, if attempts_left is 0 (meaning the loop finished without breaking), print "Account locked.".
(Hint: You'll need input() to get user text input, and int() for number input if you were getting numbers, but passwords are strings. Also, remember to handle potential ValueError if using int() for numeric input, though not strictly needed for this string password example).''')

correct_password = "mysecret"
attempts_left = 3
while attempts_left > 0:
    entered_password = input("Enter password: ")
    if entered_password == correct_password:
        print("correct_password!. Access granted!")
        break
    else:
        attempts_left -= 1
        print(f"Incorrect password. Attempts left: {attempts_left}")
if attempts_left == 0:
    print("Account locked.")

print(''' Exercise 3: Challenge: 
      Skip Negatives: Use a for loop that iterates through numbers from -5 to 5 (inclusive) using range(). Inside the loop, use a continue statement to skip printing negative numbers. Only print non-negative numbers.''')
for number in range(-5, 6):
    if number < 0:
        continue  # Skip negative numbers
    print(f"Non-negative number: {number}")
