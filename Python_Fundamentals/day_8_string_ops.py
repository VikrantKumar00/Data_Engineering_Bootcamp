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

# ----- Exercises -----

print("\n--- Exercises ---")

print('''Exercise : Create a new Python file named day_8_exercises.py in your Python_Fundamentals folder and write code for the following:

Email Formatting:
Take an email address raw_email = " User.Name@EXAMPLE.COM ".
Use string methods to clean it: remove leading/trailing spaces, convert to lowercase. Print the cleaned email.
Data Extraction:
You have a log entry: log_entry = "ERROR: File 'config.json' not found in path /app/data"
Extract the filename 'config.json' from this string using find() and string slicing, or split(). Print the extracted filename. (Hint: log_entry[start:end] is string slicing).
Path Builder:
You have a list of directories (imagine these are parts of a file path): dir_parts = ["home", "user", "documents", "reports"]
Use the join() method to combine them into a Unix-style file path (e.g., /home/user/documents/reports). Print the full path.
Data Validation:
You receive a user input string for a product code: product_code_input = "PROD123".
Check if the product_code_input starts with "PROD" AND if the remaining part (after "PROD") consists only of digits. Print True or False. (Hint: product_code_input[4:] would give you "123").''')

raw_email = " User.Name@EXAMPLE.COM "
cleaned_email = raw_email.strip().lower()
print(f'Cleaned Email: "{cleaned_email}"')

log_entry = "ERROR: File 'config.json' not found in path /app/data"
start_index = log_entry.find("'")
end_index = log_entry.find("'", start_index + 1)
extracted_data = log_entry[start_index+1:end_index]
print(extracted_data)

dir_path = ["home","user","documents","reports"]
full_path = "/"+"/".join(dir_path)
print(full_path)

product_code_input = "PROD123"
if product_code_input.startswith("PROD") and product_code_input[4:].isdigit()  == True:
    print(True)
else:
    print(False)


