# Function to read scores from the file
def read_scores():
    try:
        with open('high_scores.txt', 'r') as file:
            return [line.strip().split(',') for line in file]
    except FileNotFoundError:
        return []

# Function to write scores to the file
def write_scores(scores):
    with open('high_scores.txt', 'w') as file:
        for entry in scores:
            file.write(f"{entry[0]},{entry[1]}\n")

# Function to add a new score
def add_score(name, score):
    scores = read_scores()

    # Validate input
    if not name.isalpha() or not score.isdigit():
        print("Invalid input. Please enter a valid name and numeric score.")
        return

    # Check for duplicate names
    for i, entry in enumerate(scores):
        if entry[0] == name and int(entry[1]) < int(score):
            # Replace lower score with the higher score
            scores[i] = [name, score]
            print(f"Score for {name} updated successfully.")
            break
    else:
        # Add a new entry
        scores.append([name, score])
        print(f"Score for {name} added successfully.")

    # Sort scores in descending order
    scores.sort(key=lambda x: int(x[1]), reverse=True)

    # Write scores back to the file
    write_scores(scores)

# Function to search for a player's score
def search_score(name):
    scores = read_scores()

    for entry in scores:
        if entry[0] == name:
            return f"Score for {name}: {entry[1]}"

    return f"No score found for {name}."

# Function to display high score list in descending order
def display_high_scores():
    scores = read_scores()

    if not scores:
        print("No high scores available.")
        return

    print("\nHigh Scores (Descending Order):")
    for i, entry in enumerate(scores):
        print(f"{i+1}. {entry[0]} - {entry[1]}")

# User interface
while True:
    print("\nHigh Score Manager")
    print("1. Add New Score")
    print("2. Search Score")
    print("3. Display High Scores")
    print("4. Exit")
    choice = input("Enter your choice (1, 2, 3, or 4): ")
    if choice == '1':
        name = input("Enter player name: ")
        score = input("Enter player score: ")
        add_score(name, score)
    elif choice == '2':
        name = input("Enter player name to search: ")
        result = search_score(name)
        print(result)
    elif choice == '3':
        display_high_scores()
    elif choice == '4':
        print("Exiting High Score Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
