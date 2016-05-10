#! /usr/bin/env python3
import random

class hashtable(object):
    __slots__ = ['size', 'data']
    def __init__(self, size = 79):
        self.size = size
        self.data = [[]] * size # stores the actual data
    def _hash(self, item):
        return hash(item) % self.size
    def __setitem__(self, key, value):
        chain = self.data[self._hash(key)]
        if key in chain:
            chain[key] = (key, value)
        else:
            chain.append((key,value))
    def __getitem__(self,key):
        chain = self.data[self._hash(key)]
        matches = [i[1] for i in chain if i[0] == key]
        if len(matches) < 1:
            raise KeyError
        assert len(matches) == 1
        return matches[0]


        
d = {random.randint(0,100): random.randint(0,100) for i in range(100)}
h = hashtable(2**27)
for key in d:
    h[key] = d[key]

for key in d:
    print("%d - %d : %d" % (key, d[key], h[key]))
    assert h[key] == d[key]

