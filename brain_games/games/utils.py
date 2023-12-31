from random import randrange, choice


def get_random_num(min_num: int, max_num: int) -> int:
    return randrange(min_num, max_num + 1)


def get_random_elem(arr: list, index=False):
    if index:
        i = randrange(len(arr))
        return (arr[i], i)
    return choice(arr)
