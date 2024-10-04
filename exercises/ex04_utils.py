"""List utilities!!!"""


def all(ints: list[int], n: int) -> bool:
    for i in ints:
        if i != n:
            return False
    return True


def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    x = input[0]
    for n in input:
        if n > x:
            x = n
    return x


def is_equal(list1: list[int], list2: list[int]) -> bool:
    if len(list1) != len(list2):
        return False
    for i in range(0, len(list1)):
        if list1[i] != list2[i]:
            return False
    return True


def extend(list1: list[int], list2: list[int]) -> None:
    for i in list2:
        list1.append(i)
