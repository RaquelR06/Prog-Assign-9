# filename: 05_Dictionaries_Investigate_1.py
"""
Activity: Investigate the Code

1. Run this code and observe the three different outputs.
2. Answer the questions below in comments.

Questions:
1. What kind of items does the loop `for key in inventory.keys():` iterate over?
   # Your Answer Here

2. What kind of items does the loop `for value in inventory.values():` iterate over?
   # Your Answer Here

3. The loop `for key, value in inventory.items():` gives you two variables at once.
   What does each variable represent?
   # Your Answer Here
"""

inventory = {
    "apples": 5,
    "oranges": 3,
    "bananas": 10
}

print("--- Iterating over keys ---")
for key in inventory.keys():
    print(key)

print("\n--- Iterating over values ---")
for value in inventory.values():
    print(value)

print("\n--- Iterating over items (key-value pairs) ---")
for key, value in inventory.items():
    print(f"Item: {key}, Quantity: {value}")
