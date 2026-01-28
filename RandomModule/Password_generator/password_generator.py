import random

# Function to generate 2 unique symbols
def generate_symbols():
    symbols = ['@', '#', '!', '%', 'π', '_', '-']
    unique_symbols = random.sample(symbols, 2)  # picks 2 unique
    random.shuffle(unique_symbols)              # shuffle them
    return unique_symbols

# Function to randomize letter case
def randomize_case(word):
    while True:
        new_word = ""
        for c in word:
            new_word += c.upper() if random.choice([True, False]) else c.lower()
        # Ensure it's not all upper or all lower
        if not new_word.isupper() and not new_word.islower():
            return new_word

# Main loop
while True:
    print(f"{'*'*15} Welcome to password generator {'*'*15}")

    # Input validation loop
    while True:
        word = input("Enter any random word (no personal info) : ").replace(" ", "")
        if not word:
            print("Please enter a word!")
            continue

        num = input("Enter any random 2-digit number (10-99) : ").strip()
        if not num.isdigit() or not (10 <= int(num) <= 99):
            print("Please enter a valid 2-digit number!")
            continue

        break  # exit inner loop for valid input

    # Randomize case of the word
    word = randomize_case(word)

    # Generate symbols
    symbols = generate_symbols()

    # add one 0 to the left of original number
    num = num.zfill(3)

    # Combine symbols and number digits, and shuffle
    extras = symbols + list(num)
    random.shuffle(extras)

    # Split shuffled extras ; half before word, half after
    before_word = ''.join(extras[:2])
    after_word  = ''.join(extras[2:])

    # Print the password 
    print(f"Password generated: {before_word}{word}{after_word}")

    # Ask if user wants another password
    choice = input("Do you want to generate another password? (yes/no): ").lower()
    if choice == 'no':
        print(f"{'*'*20} Thank you for using {'*'*20}\n")
        break #exit the program
