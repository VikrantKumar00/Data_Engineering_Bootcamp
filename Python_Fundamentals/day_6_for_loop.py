# ----- Looping through a String -----

print("--- Looping through a String ---")

word = "Python"
for char in word:
    print(f"Character: {char}")

# ----- Looping through a List (introduction to lists, more details later) -----

print("\n--- Looping through a List ---")

# A list is ordered collection of items
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
for fruit in fruits:
    print(f"I like {fruit}s!")

# ----- Looping using range() - stop argument -----

for i in range(5):  # Generates 0, 1, 2, 3, 4
    print(i)

# ----- Looping using range() - start and stop arguments -----

for num in range(2, 10):  # Generates 2, 3, 4, 5, 6, 7, 8, 9
    print(num)

# ----- Looping using range() - start, stop, and step arguments -----

for even_num in range(0, 20, 2):  # Generates 0, 2, 4, ..., 18
    print(even_num)

# ----- Using enumerate() with for loops (Useful for getting index and items) -----

print("\n--- Looping with enumerate (getting index and value) ---")

colors = ["red", "green", "blue", "yellow"]
for index, color in enumerate(colors):
    print(f"Color at index {index} is {color}")


# -----  Using else with for loops (executes if the loop completes without a break) -----

print("\n--- For Loop with Else ---")

for j in range(3):
    print(f"Iteration {j}")
else:
    print("Loop finished normally (no 'break' encountered).")

# Example where else won't execute (due to break)
print("\n--- For Loop with else (but with break) ---")

for k in range(5):
    if k == 3:
        print("Breaking the loop at 3")
        break
    print(f"Iteration {k}")
else:
    print("This 'else' block will NOT be executed.")  # This line won't print


# ----- Practice Exercise -----

print("\n--- Practice Exercise ---")

print(''' Exercise 1: Repeat Name: Print your name 7 times using a for loop and the range() function.''')

my_name = "Victor"
for i in range(7):
    print(my_name)

print(''' Exercise 2: Sum of Numbers: Calculate the sum of all numbers from 1 to 50 (inclusive) using a for loop. Initialize a variable total_sum = 0 before the loop and add each number inside the loop. Print the final total_sum.''')

total_sum = 0
for number in range(1, 51):
    total_sum  = total_sum + number
final_total_sum = total_sum
print(f"The sum of numbers from 1 to 50 is: {final_total_sum}")

print(''' Exercise 3: Even Numbers: Print all even numbers between 0 and 20 (inclusive) using a for loop and the step argument in range().''')

for even_number in range(0, 21, 2):
    print(even_number)

print(''' Exercise 4:----------- Challenge:---------------
          Factorial: Write a program to calculate the factorial of a given number (e.g., 5! = 5 * 4 * 3 * 2 * 1 = 120). You can hardcode my_number = 5. Use a for loop.''')

my_number = 12
factorial_result = 1
alternate_factorial_result = 1
for i in range(1, my_number + 1):
    factorial_result = factorial_result * i
    alternate_factorial_result *= i  # Using the shorthand operator
print(f"The factorial of {my_number} is: {factorial_result}")
print(f"The factorial of {my_number} using alternate method is: {alternate_factorial_result}")

