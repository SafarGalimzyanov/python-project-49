from random import randrange, choice


def get_random_num(min_num: int, max_num: int) -> int:
    return randrange(min_num, max_num + 1)


def get_random_elem(l: list, index=False):
    if index:
        return (l[randrange(len(l))], randrange(len(l)))
    return choice(l)
