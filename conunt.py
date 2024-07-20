def count_spaces_letters(input_string):
    # Convert the string to lowercase to avoid distinguishing between uppercase and lowercase
    input_string = input_string.lower()
    
    # Initialize the counts
    space_count = 0
    letter_count = 0
    
    # Iterate through the string and count the spaces and letters
    for char in input_string:
        if char.isspace():
            space_count += 1
        elif char.isalpha():
            letter_count += 1
    
    return space_count, letter_count

# Example usage:
input_string = "The semantic similarity between frontier objects and the target object can better guide the agents exploration"
input_string = "Chat Describer can describe the spatial relationships between objects in more detail."
spaces, letters = count_spaces_letters(input_string)
print(f"空格: {spaces}, 字母: {letters}")

