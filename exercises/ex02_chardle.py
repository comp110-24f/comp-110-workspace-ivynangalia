"""EX02 - Chardle - A cute step towrd Wordle."""

__author__ = "730670491"


def input_word() -> str:
    inp: str = input("Enter a 5-character word: ")
    if len(inp) != 5:
        print("Error: Word must contain 5 characters.")
        exit()
    print(f"'{inp}'")
    return inp


def input_letter() -> str:
    inp: str = input("Enter a single character: ")
    if len(inp) != 1:
        print("Error: Character must be a single character.")
        exit()
    print(f"'{inp}'")
    return inp


def contains_char(word: str, letter: str) -> None:
    count: int = 0
    print(f"Searching for {letter} in {word}")
    for i in range(0, len(word)):
        if word[i] == letter:
            count += 1
            print(f"{letter} found at index {i}")
    if count == 0:
        print(f"No instances of {letter} found in {word}")
    else:
        print(f"{count} instances of {letter} found in {word}")


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
