import json
from pprint import pprint

from dt_learning import dt_learning, prettyprint_tree

if __name__ == '__main__':
    u10 = '< 10'
    b1020 = '10 - 20'
    o20 = '> 20'
    false = 'F'
    true = 'T'

    data = {
        'Enemy visible': ["0", "0", "0", "0", "0", "0", "1", "1", "1", "1", "1", "1"],
        'Enemy distance': [u10, u10, b1020, b1020, o20, o20, u10, u10, b1020, b1020, o20, o20],
        'Enemy armed': ["0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1"],
        'Attack': [true, false, false, false, false, false, true, true, true, true, false, false]
    }

    attributes = columns = ["Enemy visible", "Enemy distance", "Enemy armed"]
    attributes.append("Attack")

    decisionTree = dt_learning(data, attributes)
    prettyprint_tree(decisionTree)
