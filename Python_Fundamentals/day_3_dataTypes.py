user_name = "Vikrant Kumar"
user_age = 26


print("--- Numbers Operations ---")

num1 = 10
num2 = 3.5
num3 = 6

print(f"num1 (int): {num1}, Type: {type(num1)}")
print(f"num2 (float): {num2}, Type: {type(num2)}")

print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} * 2 = {num1 * 2}")
print(f"{num1} / {num2} = {num1 / num2}")
print(f"{num1} // {num2} = {num1 // num2}")  # Floor division
print(f"{num1} // {num3} = {num1 // num3}")  # Floor division with int
print(f"10 % 3 = {10 % 3}  (Remainder)")
print(f"2 ** 3 = {2 ** 3}  (2 to the power of 3)")


print("\n--- Strings Operations ---")
greeting = "Hello"
user_name = "Vikrant Kumar"
space = " "

full_message = greeting + space + user_name + "!"
print(f"Concatenated message: {full_message}")

reapeted_word = "Python" * 3
print(f"Repeated word: {reapeted_word}")

# Multi-line string

long_text = """This is a long text"
It can span multiple lines.
It is useful for documentation or comments."""
print(f"\nMulti-line string:\n{long_text}")

print("\n----- Exercise -----\n")

# Create two variables, fav_int storing your favorite integer and fav_float storing your favorite decimal number. Perform addition, multiplication, and standard division (/) with them. Print the result of each operation with a clear label (e.g., print(f"Sum: {fav_int + fav_float}")).
fav_int = 7
fav_float = 3.14

print(f"Sum: {fav_int + fav_float}")
print(f"Multiplication: {fav_int * fav_float}")
print(f"Division: {fav_int / fav_float}")

# Create two string variables, first_name and last_name. Concatenate them with a space in between to print your full name.
first_name = "Vikrant"
last_name = "Kumar"
full_name = first_name + " " + last_name
print(f"Full Name: {full_name}")

# Print a short phrase, like "Data is Fun!", four times using the string repetition operator.
print(f"data is Fun! " * 4)