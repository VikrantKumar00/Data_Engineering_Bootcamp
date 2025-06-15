# ----- Basic if statement -----

print("--- Basic if statement ---")

user_age = 23
if user_age >= 18:
    print("You are eligible to vote.")

# ----- if-else statement -----

print("\n--- if-else statement ---")

current_temperature = 22
if current_temperature > 30:
    print("It's a hot day.")
else:
    print("It's a pleasant temperature.")

# ----- if-elif-else statement -----

student_score = 85

if student_score >= 90:
    print("Grade: A - Excellent!")
elif student_score >= 80:
    print("Grade: B - Very Good!")
elif student_score >= 70:
    print("Grade: C - Good!")
elif student_score >= 60:
    print("Grade: D - Passable!")
else:
    print("Grade: F - Needs Improvement!")


# ----- Combining conditions with logical operators -----

print("\n--- Combined Conditions ---")

is_premium_member = True
purchase_amount = 125.50

if is_premium_member and purchase_amount > 100:
    print("You qualify for a special premium discount!")
elif is_premium_member or purchase_amount > 50:
    print("You got a standard discount!")
else:
    print("No discounts today, but keep shopping!")


# ----- Nested if statements(use sparingly for readability) -----

print("\n--- Nested if statements ---")

has_ticket = True
is_vip = True

if has_ticket:
    print("Welcome! You have a ticket.")
    if is_vip:
        print("Please proceed to the VIP lounge.")
    else:
        print("Enjoy the main area.")
else:
    print("Sorry, no ticket, no entry.")


# ----- Exercises -----

print("\n--- Exercises ---")

print('Exercise 1: Write a program that takes a number (you can hardcode it as a variable for now, e.g., my_number = -5) and prints whether it\'s "Positive", "Negative", or "Zero".')

my_number = -5
if my_number > 0:
    print("Positive")
elif my_number < 0:
    print("Negative")
else:
    print("Zero")

print(f"Exercise 2: Traffic Light Simulator: Imagine a traffic light. Write a program that takes a color (e.g., light_color = 'yellow'). Use if-elif-else to print what action a driver should take: 'red': 'Stop! Wait for green light.'\
    'yellow': 'Prepare to stop, or clear intersection if safe.'\
    'green': 'Go! Proceed safely.'\
    Any other color: 'Invalid traffic light color.'")
light_color = input("Enter the traffic light color (red, yellow, green): ").strip().lower()
if light_color == 'red':
    print("Stop! Wait for green light.")
elif light_color == 'yellow':
    print("Prepare to stop, or clear intersection if safe.")
elif light_color == 'green':
    print("Go! Proceed safely.")
else:
    print("Invalid traffic light color.")

print("----------Challenge 3 ----------")

print('''Challenge - Simple Login System:
    Define a stored_username = "admin" and stored_password = "password123".
    For now, hardcode entered_username = "admin" and entered_password = "password123" (we'll learn user input later).
    Use an if statement with a logical operator (and) to check if both entered_username matches stored_username AND entered_password matches stored_password.
    If they both match, print "Login successful! Welcome, admin!".
    Otherwise, print "Login failed. Invalid username or password.".
    Test with both correct and incorrect credentials.''')

stored_username = "admin"
stored_password = "password123"

entered_username = "admin"
entered_password = "password123"

if entered_username == stored_username and entered_password == stored_password:
    print("Login successful! Welcome, admin!")
else:
    print("Login failed. Invalid username or password.")
    print("Please try again.")

