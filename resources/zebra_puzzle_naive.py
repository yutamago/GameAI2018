# Solution of Einstein's Zebra Puzzle (http://en.wikipedia.org/wiki/Zebra_Puzzle)

import itertools


def imright(h1, h2):
    return h1 - h2  == 1


def nextto(h1, h2):
    return abs(h1 - h2) == 1


def zebra_puzzle_slow():
    houses = [first, _, middle, _, _] = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(houses))
    return next((WATER, ZEBRA)
                for (Englishman, Spaniard, Ukrainian, Japanese, Norwegian) in orderings
                for (red, green, ivory, yellow, blue) in orderings
                for (dog, snails, fox, horse, ZEBRA) in orderings
                for (coffee, tea, milk, oj, WATER) in orderings
                [...]
                )


if __name__ == '__main__':
    print(zebra_puzzle_slow())
