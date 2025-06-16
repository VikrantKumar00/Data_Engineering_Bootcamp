# ----- Basic String Operations -----

my_string = "   Hello, Data Engineers!  "
print(f"Original string: '{my_string}'")
print(f"Length of string: {len(my_string)}")


# ----- Case Conversion Methods -----

print("\n--- Case Conversions ---")

print(f"Lowercase: '{my_string.lower()}'")
print(f"Uppercase: '{my_string.upper()}'")
print(f"Capitalized: '{my_string.capitalize()}'")
print(f"Title Case: '{my_string.title()}'")


# ----- Whitespace Removal Methods -----

print("\n--- Whitespace Removal ---")
cleaned_string = my_string.strip()
print(f"Stripped string: '{cleaned_string}'")
print(f"Left stripped: '{my_string.lstrip()}'")
print(f"Right stripped: '{my_string.rstrip()}'")

csv_header = "Name,Age,City,Occupation"
columns = csv_header.split(',')
print(f"CSV Columns: {columns}")

# Joining elements of a list into a string

new_message_parts = ["Hello", "World", "Python"]
joined_message_space = " ".join(new_message_parts)
joined_message_dash = "-".join(new_message_parts)
print(f"Joined with space: '{joined_message_space}'") 
print(f"Joined with dash: '{joined_message_dash}'")

# ----- Searching and Replacing ------

print("\n--- Searching and Replacing ---")
sentence = "Python is powerful. Python is versatile."
print(f"Original sentence: '{sentence}'")
print(f"Index of 'powerful': {sentence.find('powerful')}") # returns the starting index
print(f"Index of 'Java'(not found): {sentence.find('Java')}") # returns -1 if not found

count_python = sentence.count("Python")
print(f"Number of 'Python' occurrences: {count_python}")

# ------Checking Content ------

print("\n--- Checking Content ---")
file_name = "report.csv"
user_id = "user123"
valid_number = "12345"
mixed_string = "Pyth0n"

print(f"'{file_name}' ends with '.csv'? {file_name.endswith('.csv')}")
print(f"'{user_id}' starts with 'user'? {user_id.startswith('user')}")
print(f"'{valid_number}' is digit? {valid_number.isdigit()}")
print(f"'{mixed_string}' is alphabetic? {mixed_string.isalnum()}")

# ----- String Immutability Demo -------

print("\n--- String Immutability Demo ---")
original_text = "Data"
modified_text = original_text.upper()
print(f"Original text: '{original_text}'")
print(f"Modified text: '{modified_text}'")
