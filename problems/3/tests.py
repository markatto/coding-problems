#! /usr/bin/env python3
from incr_dict import incr_dict
from incr_dict import RecursiveDefaultDict
import timeit
import random
import string
import unittest

class IncrDictTests(unittest.TestCase):
    def moat_test(self):
        '''test examples from the pdf'''
        dct = {}
        rdd = RecursiveDefaultDict()

        incr_dict(dct, ('a', 'b', 'c')) 
        rdd['a']['b']['c'] += 1
        r = {'a': {'b': {'c': 1}}}
        self.assertEquals(dct, r)
        self.assertEquals(rdd, r)

        incr_dict(dct, ('a', 'b', 'c')) 
        rdd['a']['b']['c'] += 1
        r = {'a': {'b': {'c': 2}}}
        self.assertEquals(dct, r)
        self.assertEquals(rdd, r)

        incr_dict(dct, ('a', 'b', 'f')) 
        rdd['a']['b']['f'] += 1
        r = {'a': {'b': {'c': 2, 'f': 1}}}
        self.assertEquals(dct, r)
        self.assertEquals(rdd, r)

        incr_dict(dct, ('a', 'r', 'f')) 
        rdd['a']['r']['f'] += 1
        r = {'a': {'r': {'f': 1}, 'b': {'c': 2, 'f': 1}}}
        self.assertEquals(dct, r)
        self.assertEquals(rdd, r)

        incr_dict(dct, ('a', 'z')) 
        rdd['a']['z'] += 1
        r = {'a': {'r': {'f': 1}, 'b': {'c': 2,'f': 1}, 'z': 1}}
        self.assertEquals(dct, r)
        self.assertEquals(rdd, r)

    def empty_tuple_test(self):
        '''test behavior with an empty tuple argument'''
        dct = {}
        incr_dict(dct, ())
        self.assertEquals(dct, {})
        incr_dict(dct, ('a',))
        self.assertEquals(dct,{'a': 1})
        incr_dict(dct, ())
        self.assertEquals(dct, {'a': 1})
        
        # rdd doesn't really have an equivalent of this

    def increment_node_with_children_test(self):
        '''test behavior of incrementing a node that has children'''
        #behavior for this case is unspecified; the implementations handle it differently

        d = {}
        rdd = RecursiveDefaultDict()

        # incr_dict raises a TypeError when you try to add an int to a dict
        incr_dict(d, ('a', 'b'))
        with self.assertRaises(TypeError): 
            incr_dict(d, ('a',))

        # this operation is supported because of our __add__ hack in rdd, but
        # all children of the node you're incrementing are lost
        rdd ['a']['b'] += 1
        self.assertEquals(rdd, {'a': {'b': 1}})
        rdd ['a'] += 1
        self.assertEquals(rdd, {'a': 1})

    def large_tuple_test(self):
        '''test performance for a large tuple argument'''
        dct = {}
        big_tuple = [random.choice(string.ascii_letters) for i in range(1000000)] #totally a tuple
        t = timeit.Timer(lambda: incr_dict(dct, big_tuple), 'gc.enable()')
        runtime =  t.timeit(number=1)
        assert runtime < 10 # fail if it takes >= 10s to insert 1m items

        # crazy hack to check performance of the rdd implementation
        # due to maximum recursion depth there's a limit to how deep we can go here
        rdd_test_tuple = [random.choice(string.ascii_letters) for i in range(1000)]
        test_string = 'from incr_dict import RecursiveDefaultDict;'
        test_string += 'rdd = RecursiveDefaultDict(); rdd' 
        test_string += ''.join(('["{}"]'.format(key) for key in rdd_test_tuple)) + ' += 1'
        t = timeit.Timer(test_string, 'gc.enable()')
        assert t.timeit(number=100) < 10 # fail if it takes >= 10s to insert 1k items 100 times
