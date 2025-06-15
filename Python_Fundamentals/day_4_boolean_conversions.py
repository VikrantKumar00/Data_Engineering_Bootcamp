# --- Boolean and Comparisons Operations ---

print("--- Boolean and Comparison ---")

num_a = 50
num_b = 50
num_c = 100

print(f"Is num_a equal to num_b? {num_a == num_b}")
print(f"Is num_a not equal to num_c? {num_a != num_c}")
print(f"Is num_c greater than num_a? {num_c > num_a}")
print(f"Is num_a less than or equal to num_b? {num_a <= num_b}")


# ----- Logical Operators -----

print("\n--- Logical Operators ---")
is_morning = True
is_weekday = False
is_tired = True

# Are both True?
should_go_to_work = is_morning and is_weekday
print(f"Should go to work (morning AND weekday)? {should_go_to_work}")

# Is it least one True?
can_relax = not is_weekday or is_tired
print(f"Can relax (NOT weekday OR tired)? {can_relax}")

# Opposite of a boolean

is_awake = not is_tired
print(f"Is awake (NOT tired)? {is_awake}")

# ----- Type Conversions -----

print("\n--- Type Conversions ---")
price_str = "25.99"
quantity_str = "3"
user_input_age = "26"
some_number = 0
some_text = "Python"
empty_string = ""

# String to number conversion

total_price = float(price_str) * int(quantity_str)
print(f"Converted price to float, quantity to int. Total price: {total_price}")

#Number to string 
product_id = 12345
product_code = "PROD-" + str(product_id)
print(f"Integer converted to string for concatenation: {product_code}")

#Various to boolean conversions

print(f"bool(0) is {bool(some_number)}")
print(f"bool('Python') is {bool(some_text)}")
print(f"bool('') is {bool(empty_string)}")
print(f"bool('False') is {bool('False')}")  # A non-empty string is Always True

# String to integer conversion

age_in_int = int(user_input_age)
print(f"User input age(string) as integer: {age_in_int}")

# Exercising

print("\n--- Exercise: Boolean and Type Conversions ---")

print(f"Question 1: Create two numeric variables, num_x = 15 and num_y = 7. Use comparison operators (>, <, ==, !=, >=, <=) to compare them. Print the boolean result of each comparison with a descriptive label.")

num_x = 15
num_y = 7

print(f"Is num_x greater than num_y? {num_x > num_y}")
print(f"Is num_x less than num_y? {num_x < num_y}")
print(f"Is num_x equal to num_y? {num_x == num_y}")
print(f"Is num_x not equal to num_y? {num_x != num_y}")
print(f"Is num_x greater than or equal to num_y? {num_x >= num_y}")
print(f"Is num_x less than or equal to num_y? {num_x <= num_y}")

print(f"\nQuestion 2: Create two boolean variables: is_raining = True and has_coat = False. Use logical operators to check and print: If it's raining AND you have a coat. If it's raining OR you have a coat. If it's NOT raining.")

is_raining = True
has_coat = False
print(f"Is it raining AND do you have a coat? {is_raining and has_coat}")
print(f"Is it raining OR do you have a coat? {is_raining or has_coat}")
print(f"Is it NOT raining? {not is_raining}")

print(f"\nQuestion 3: Take a string height_str = '175' and convert it to an integer. Add 5 to it and print the result.")

height_str = "175"
height_int = int(height_str)
print(f"Height after adding 5: {height_int + 5}")

print(f"\nQuestion 4: Take an integer item_count = 10 and convert it to a string. Concatenate it with 'Total items: ' and print the result.")

item_count = 10
item_count_str = str(item_count)
print(f"{"Total items: " + item_count_str}")
