def find_optimal_speed(piles, hours):
    """
    solves task from README.md

    :param piles: list of piles with bananas
    :param hours: hours monkey has to eat all bananas.gitignore
    :return: minimal most suitable value to pass task condition

    >>> find_optimal_speed([3, 6, 7, 11], 8)
    4
    >>> find_optimal_speed([30, 11, 23, 4, 20], 5)
    30
    >>> find_optimal_speed([30, 11, 23, 4, 20], 6)
    23
    >>> find_optimal_speed([5, 6], 2)
    6
    >>> find_optimal_speed([5, 6], 3)
    5
    """
    min_speed = 1
    max_speed = max(piles)
    return binary_search(min_speed, max_speed, piles, hours)


def binary_search(minimal_value, maximal_value, piles, hours):
    """
    finds minimal most suitable value to pass task condition

    :param minimal_value: minimal value to start search from (1)
    :param maximal_value: maximal value of bananas in piles
    :param piles: list of piles with bananas
    :param hours: hours monkey has to eat all bananas
    :return: minimal most suitable value to pass task condition

    >>> binary_search(1, 11, [3, 6, 7, 11], 8)
    4
    """
    while minimal_value <= maximal_value:
        probable_speed = (minimal_value + maximal_value) // 2
        if can_eat_in_time(piles, hours, probable_speed):
            maximal_value = probable_speed - 1
        else:
            minimal_value = probable_speed + 1
    return minimal_value


def can_eat_in_time(piles, hours_to_eat, probable_speed):
    """
    checks condition if monkey can eat all bananas with eating speed of probable_speed in hours_to_eat

    :param piles: list of piles with bananas
    :param hours_to_eat: hours monkey has to eat all bananas
    :param probable_speed: speed to check
    :return: true if pass condition else false

    >>> can_eat_in_time([3, 6, 7, 11], 8, 6)
    True
    >>> can_eat_in_time([3, 6, 7, 11], 8, 3)
    False
    """
    real_hours = 0
    for pile in piles:
        if pile % probable_speed == 0:
            real_hours += int(pile / probable_speed)
        else:
            real_hours += int(pile / probable_speed) + 1
    return real_hours <= hours_to_eat


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
