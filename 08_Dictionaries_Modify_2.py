# filename: 08_Dictionaries_Modify_2.py
"""
Activity: Modify the Code

If you run this code and type a word that isn't in the dictionary (like "cat"),
it will crash with a KeyError.

Your goal:
1.  Modify the code to check if the `user_word` exists as a key in the `definitions`
    dictionary *before* you try to access it.
2.  Use an `if/else` statement.
    - If the key exists, print its definition.
    - If the key does not exist, print a friendly message like "Sorry, that word is not defined."

Hint: You can check if a key is in a dictionary like this: `if key in my_dict:`
"""

definitions = {
    "python": "A high-level programming language.",
    "list": "A collection of ordered, changeable items in Python."
}

user_word = input("Enter a word to define: ")

# --- MODIFY THE CODE BELOW ---

# This line will crash if the user_word is not a key!
print(definitions[user_word])

# --- END MODIFICATION ---
