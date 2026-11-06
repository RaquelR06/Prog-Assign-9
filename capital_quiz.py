import random

def main():
    # Create a dictionary of U.S. States and their capitals
    capitals = {
        'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
        'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
        'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
        'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
        'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines',
        'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge',
        'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston',
        'Michigan': 'Lansing', 'Minnesota': 'St. Paul', 'Mississippi': 'Jackson',
        'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln',
        'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
        'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
        'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
        'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
        'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville',
        'Austin': 'Texas', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier',
        'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
        'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'
    }

    correct_count = 0
    incorrect_count = 0

    # Get a list of the states (keys)
    states = list(capitals.keys())

    print("Welcome to the State Capital Quiz!")
    print("Type 'quit' to exit the quiz.\n")

    while True:
        # Pick a random state
        state = random.choice(states)
        correct_capital = capitals[state]

        # Ask the user for the capital
        user_answer = input(f"What is the capital of {state}? ").strip()

        if user_answer.lower() == 'quit':
            break

        # Check if the answer matches (case-insensitive)
        if user_answer.lower() == correct_capital.lower():
            print("Correct!\n")
            correct_count += 1
        else:
            print(f"Incorrect. The capital of {state} is {correct_capital}.\n")
            incorrect_count += 1

    # Print final score summary
    print("\n--- Quiz Over ---")
    print(f"Total Correct: {correct_count}")
    print(f"Total Incorrect: {incorrect_count}")

if __name__ == '__main__':
    main()
    
