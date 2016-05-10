#! /usr/bin/env python3

def incr_dict(d, keys):
    '''incr_dict(dct, ('a', 'b', 'c')) ~= dct['a']['b']['c'] += 1'''
    if len(keys) < 1:
        # nothing to do
        return

    parent = d
    for key in keys[:-1]:
        if not key in parent:
            parent[key] = {}
        parent = parent[key]

    last_key = keys[-1]
    if not last_key in parent:
        parent[last_key] = 0
    parent[last_key] += 1

# The problem can also be solved in a slightly more elegant fashion
# by subclassing dict. Note that there are some performance and recursion
# depth limitations to this approach due to each layer requiring a function
# call.
# I would love to play with monkey patching dicts in dirty ways,
# but sadly dict is a builtin.
class RecursiveDefaultDict(dict):
    def __missing__(self, key):
        '''default value is an instance of ourself'''
        self[key] = RecursiveDefaultDict()
        return self[key]

    def __add__(self, arg):
        '''adding x to this results in x (makes += work)'''
        return arg
