import random


def main():
    numbers = [16.2, 75.1, 52.3]
    print(f"Initial numbers list: {numbers}")

    append_random_numbers(numbers)
    print(f"After adding one random number: {numbers}")

    append_random_numbers(numbers, 3)
    print(f"After adding three random numbers: {numbers}")

    words = ["Chad", "Efe", "Joyce", "Natalie"]
    print(
        f"\nInitial words list: {words}",
    )

    append_random_words(words)
    print(
        f"After adding one random word: {words}",
    )

    append_random_words(words, 3)
    print(
        f"After adding three random words: {words}",
    )


def append_random_numbers(numbers_list, quantity=1):
    for _ in range(quantity):
        random_number = round(random.uniform(0, 100), 1)
        numbers_list.append(random_number)


def append_random_words(words_list, quantity=1):
    word_list = ["Johnson", "Enahoro", "Jensen", "Kija"]
    for _ in range(quantity):
        random_word = random.choice(word_list)
        words_list.append(random_word)


if __name__ == "__main__":
    main()
