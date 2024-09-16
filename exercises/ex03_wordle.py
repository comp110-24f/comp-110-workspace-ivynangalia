"""Wordle, i guess."""


def input_guess(secret_word_len: int) -> str:
    input_word: str = input(f"Enter a {secret_word_len} character word: ")
    while len(input_word) != secret_word_len:
        input_word = input(f"That wasn't {secret_word_len} chars! Try again: ")
    return input_word


def contains_char(word: str, char: str) -> bool:
    assert len(char) == 1
    if char in word:
        return True
    else:
        return False


WHITE_BOX: str = "\U00002B1C"  # defining emojis as global variables
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess: str, secret: str) -> str:
    result: str = ""
    assert len(guess) == len(secret)
    for i in range(0, len(secret)):
        if contains_char(word=secret, char=guess[i]):
            if guess[i] == secret[i]:
                result += GREEN_BOX
            else:
                result += YELLOW_BOX
        else:
            result += WHITE_BOX
    return result


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    for turn in range(1, 7):
        print(f"=== Turn {turn} / 6 ===")
        guess: str = input_guess(secret_word_len=len(secret))
        print(emojified(guess=guess, secret=secret))
        if guess == secret:
            print(f"You won in {turn} / 6 turns!")
            quit()
    print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
