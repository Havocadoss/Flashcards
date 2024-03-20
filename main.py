import random
import json

flashcards = {
    "capital of france": "paris",
    "capital of italy": "rome",
    "capital of spain": "madrid",
    "capital of germany": "berlin",
    "capital of the united kingdom": "london",
    "capital of the united states": "washington dc",
    "capital of australia": "canberra",
    "capital of new zealand": "wellington",
    "capital of austria": "vienna",
    "capital of belgium": "brussels",
    "capital of the netherlands": "amsterdam",
    "capital of switzerland": "bern",
    "capital of sweden": "stockholm",
    "capital of norway": "oslo",
    "capital of finland": "helsinki",
    "capital of denmark": "copenhagen",
    "capital of iceland": "reykjavik",
    "capital of northern ireland": "belfast",
    "capital of ireland": "dublin",
    "capital of scotland": "edinburgh"
}


def show_flashcards():
    flashcard_keys = list(flashcards.keys())
    random.shuffle(flashcard_keys)
    for key in flashcard_keys:
        user_response = input("What is the " + key + "? ")
        if user_response.lower() == flashcards[key]:
            print("Correct!")
        else:
            print("Incorrect. The correct answer is: " + flashcards[key])


def main():
    show_flashcards()


def leitner_system():
    flashcards_copy = dict(flashcards)
    levels = [[] for _ in range(5)]

    for key in flashcards_copy.keys():
        levels[0].append(key)

    for _ in range(4):
        for level in levels:
            for key in level:
                user_response = input("What is the " + key + "? (Type 'skip' to move to next card) ")
                if user_response.lower() == flashcards[key]:
                    print("Correct!")
                    levels[levels.index(level) + 1].append(key)
                elif user_response.lower() == 'skip':
                    levels[levels.index(level) + 1].append(key)
                else:
                    print("Incorrect. The correct answer is: " + flashcards[key])

    print("Congratulations! You have completed all flashcards.")

if __name__ == "__main__":
    main()