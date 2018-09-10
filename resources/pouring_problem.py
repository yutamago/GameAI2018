'''
Created on Sep 8, 2013

@author: pglauner
'''
import pprint

from resources.shortest_path import shortest_path_search


def successors(left_capacity: int, right_capacity: int):
    def sc(state):
        left_val, right_val = state
        assert left_val <= left_capacity and right_val <= right_capacity
        return {((0, right_val + left_val) if right_val + left_val <= right_capacity else (
            left_val - (right_capacity - right_val), (right_capacity))): 'x->y',
                ((left_val + right_val, 0) if left_val + right_val <= left_capacity else (
                    left_capacity, (right_val - (left_capacity - left_val)))): 'x<-y',
                (left_capacity, right_val): 'fill x',
                (left_val, right_capacity): 'fill y',
                (0, right_val): 'empty x',
                (left_val, 0): 'empty y'}

    return sc


if __name__ == '__main__':
    res = shortest_path_search((0, 0), successors(418, 986), lambda state: state == (6, 0))
    print(res)
    print('%s transitions' % (int(len(res) / 2)))
