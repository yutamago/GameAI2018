# Solution of Einstein's Zebra Puzzle (http://en.wikipedia.org/wiki/Zebra_Puzzle)

import itertools
import timeit


def imright(h1, h2):
    return h1 - h2 == 1


def nextto(h1, h2):
    return abs(h1 - h2) == 1


def owns(h1, h2):
    return h1 == h2


def zebra_puzzle_slow():
    houses = [first, _, middle, _, _] = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(houses))
    return next((Englishman, Spaniard, Ukrainian, Japanese, Norwegian, WATER, ZEBRA, blue)
                for (Englishman, Spaniard, Ukrainian, Japanese, Norwegian) in orderings
                if owns(Norwegian, first)

                for (red, green, ivory, yellow, blue) in orderings
                if owns(Englishman, red)
                if imright(green, ivory)
                if nextto(Norwegian, blue)

                for (oldGold, kools, chesterfields, luckyStrike, parliaments) in orderings
                if owns(kools, yellow)
                if owns(Japanese, parliaments)

                for (dog, snails, fox, horse, ZEBRA) in orderings
                if owns(Spaniard, dog)
                if owns(oldGold, snails)
                if nextto(chesterfields, fox)
                if nextto(kools, horse)

                for (coffee, tea, milk, oj, WATER) in orderings
                if owns(coffee, green)
                if owns(Ukrainian, tea)
                if owns(milk, middle)
                if owns(luckyStrike, oj)

                )


if __name__ == '__main__':
    start = timeit.timeit()

    print(zebra_puzzle_slow())

    end = timeit.timeit()
    print(end - start)
