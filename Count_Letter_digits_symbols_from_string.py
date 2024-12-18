def count_characters(input_string):
    letters = 0
    digits = 0
    special_symbols = 0

    # Iterate over each character in the input string
    for char in input_string:
        if char.isalpha():  # Check if the character is a letter
            letters += 1
        elif char.isdigit():  # Check if the character is a digit
            digits += 1
        elif not char.isspace():  # Exclude spaces from special symbols count
            special_symbols += 1

    return letters, digits, special_symbols

# Test the function with an example string
input_string = "Hello World! 1234 @#"
letters, digits, special_symbols = count_characters(input_string)

# Print the results
print(f"Letters: {letters}")
print(f"Digits: {digits}")
print(f"Special Symbols: {special_symbols}")
