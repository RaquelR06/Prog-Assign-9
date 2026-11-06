# filename: 06_Dictionaries_Investigate_2.py
"""
Activity: Investigate the Code

1. Read the code below. Notice that the key "apple" is used twice.
2. Predict what the final dictionary will look like.
3. Run the code and observe the output.
4. Answer the questions in the comments below.

Questions:
1. What happened to the first entry for "apple" (with the value "red")?
   # Your Answer Here

2. Based on this, can a dictionary have duplicate keys? What happens if you try?
   # Your Answer Here
"""

# What happens when a key is duplicated?
fruit_colors = {
    "apple": "red",
    "banana": "yellow",
    "apple": "green" # Duplicate key!
}

print("Final dictionary:", fruit_colors)
