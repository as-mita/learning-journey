import random

def get_random_quote():
    quotes = [
        "The best way to get started is to quit talking and begin doing. – Walt Disney",
        "Don’t let yesterday take up too much of today. – Will Rogers",
        "It’s not whether you get knocked down, it’s whether you get up. – Vince Lombardi",
        "If you are working on something exciting, it will keep you motivated. – Steve Jobs",
        "Success is not in what you have, but who you are. – Bo Bennett",
        "Dream bigger. Do bigger.",
        "Don’t watch the clock; do what it does. Keep going. – Sam Levenson"
    ]
    return random.choice(quotes)

def main():
    print(" Welcome to the Random Quote Generator ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    quote = get_random_quote()
    print(f"💬 {quote}")

if __name__ == "__main__":
    main()
