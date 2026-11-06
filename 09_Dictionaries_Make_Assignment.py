# filename: 09_Dictionaries_Make_Assignment.py
"""
Assignment: Character Frequency Counter

In this assignment, you will write a program that counts how many times each
character appears in a given string. You will use a dictionary to store the
results, where each character is a key and its count is the value.

Instructions:
1.  Create an empty dictionary called `char_counts`.
2.  Loop through each character of the `text_to_analyze` string.
3.  Inside the loop, for each character:
    a. Check if the character is already a key in your `char_counts` dictionary.
    b. If it is, increment the value (the count) associated with that key by 1.
    c. If it is not, add the character to the dictionary as a new key with a value of 1.
4.  After the loop, print the `char_counts` dictionary.

Example String: "hello world"
Expected Output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
(Note: The order of your dictionary might be different, and that's okay!)
"""

text_to_analyze = "programming is fun"

# 1. Initialize an empty dictionary
char_counts = {}

# --- YOUR CODE GOES BELOW ---

# 2. Loop through the string and count characters

# 4. Print the final dictionary
print("Character counts:")
print(char_counts)
