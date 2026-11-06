# filename: 04_Dictionaries_Predict_2.py
"""
Activity: Predict the Output

1.  Read the code below.
2.  Without running the code, predict the final state of the `user_profile` dictionary
    after all the operations are complete.
3.  Write your prediction in the `prediction` variable.
"""

# What will the final dictionary look like?
prediction = {} # Example: {"username": "zane", "level": 11, "active": False}

user_profile = {
    "username": "alex",
    "level": 10
}

# Add a new key-value pair
user_profile["active"] = True

# Update an existing value
user_profile["level"] = 11

print("Final user profile:", user_profile)
