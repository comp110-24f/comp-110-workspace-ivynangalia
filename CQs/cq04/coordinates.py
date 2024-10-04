"""Coordinating!"""


def get_coords(xs: str, ys: str) -> None:
    for i in xs:
        for j in ys:
            print(f"({i}, {j})")
