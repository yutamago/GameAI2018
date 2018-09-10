from resources.shortest_path import shortest_path_search

notAllowedStates = [
    (3, 0, 3, 0),
    (3, 0, 3, 0),
]


def boatyMcBoatFace(state):
    cL, cR, mL, mR = state

    print(state)
    assert cL >= 0 and cR >= 0
    assert mL >= 0 and mR >= 0
    assert mL >= cL or mL == 0
    assert mR >= cR or mR == 0

    states = {
        (cL - 1, cR + 1, mL, mR): 'c  ->',
        (cL - 2, cR + 2, mL, mR): 'cc ->',
        (cL - 1, cR + 1, mL - 1, mR + 1): 'cm ->',
        (cL + 1, cR - 1, mL, mR): 'c  <-',
        (cL + 2, cR - 2, mL, mR): 'cc <-',
        (cL + 1, cR - 1, mL + 1, mR - 1): 'cm <-'
    }

    def isIllegalMove(state):
        cL, cR, mL, mR = state
        if cL > 3 or cL < 0 \
                or cR > 3 or cR < 0 \
                or mL > 3 or mL < 0 \
                or mR > 3 or mR < 0:
            return True

        if (cL > mL and not mL == 0) or (cR > mR and not mR == 0):
            return True

        return False

    remove = [k for k in states if isIllegalMove(k)]
    for k in remove: del states[k]

    print(states)
    return states


if __name__ == '__main__':
    res = shortest_path_search((3, 0, 3, 0), boatyMcBoatFace, lambda state: state == (0, 3, 0, 3))
    print(res)
    print('%s transitions' % (int(len(res) / 2)))
