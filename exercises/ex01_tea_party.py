"""Creating a fun tea party for my 110 friends!!"""

__author__ = "730670491"


def tea_bags(people: int) -> int:
    """How many tea bags?"""
    return 2 * people  # 2 tea bags per person


def treats(people: int) -> int:
    """How many treats?"""
    return int(1.5 * tea_bags(people))  # convert back to int since 1.5 returns a float


def cost(treat_count: int, tea_count: int) -> float:
    """How much do I owe ya?"""
    return treat_count * 0.75 + tea_count * 0.5  # multiply then add


def main_planner(guests: int):
    """Plan a party!"""
    print(f"A Cozy Tea Party for {guests} People!")  # f strings
    print(f"Tea Bags: {tea_bags(guests)}")
    print(f"Treats: {treats(guests)}")
    print(f"Cost: {cost(treats(guests), tea_bags(guests))}")
