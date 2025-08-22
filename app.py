import random

def generate_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why don't skeletons fight each other? They don't have the guts.",
        "What do you call fake spaghetti? An impasta!",
        "Why did the bicycle fall over? Because it was two-tired!"
    ]
    return random.choice(jokes)

print("Welcome to the Joke Generator!")
print("Get ready to laugh!")    
print("Press Enter to get a joke...")
input()  # Wait for user to press Enter
print("Generating a joke...")   
print("Here's your joke:")
print(generate_joke())

if __name__ == "__main__":
    print("Here's a joke for you:")
    print(generate_joke())
# This code generates a random joke from a predefined list and prints it to the console.