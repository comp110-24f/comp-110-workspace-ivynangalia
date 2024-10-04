"""While loops."""


def num_instances(phrase: str, search_char: str) -> int:
    """Count the number of times search_char appears in phrase."""
    count: int = 0 # initialize count to be returned later
    idx: int = 0 # initialize index
    while idx < len(phrase): 
        if phrase[idx] == search_char:
            count += 1 
        idx += 1 # no infinite loops here
    return count
