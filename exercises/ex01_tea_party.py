"""Creating a fun tea party for my 110 friends!!"""

__author__ = "730670491"


def tea_bags(people: int) -> int:
    """How many tea bags?"""
    return 2 * people  # 2 tea bags per person


def treats(people: int) -> int:
    """How many treats?"""
    return int(
        1.5 * tea_bags(people=people)
    )  # convert back to int since 1.5 returns a float


def cost(tea_count: int, treat_count: int) -> float:
    """How much do I owe ya?"""
    return 1.00 * ((treat_count * 0.75) + (tea_count * 0.50))  # multiply then add


def main_planner(guests: int) -> None:
    """Plan a party!"""
    print(f"A Cozy Tea Party for {guests} People!")  # f strings
    print(f"Tea Bags: {tea_bags(guests)}")  # call function for x amount of guests
    print(f"Treats: {treats(guests)}")
    print(f"Cost: ${cost(tea_bags(guests), treats(guests))}")


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
