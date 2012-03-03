#!/usr/bin/python -B

from trie import Trie

""" Here's a couple of helper methods to print on assigment and dump the
    trie. You don't need in practice and can just treat the Trie as any
    other dict-like structure.
"""


def assign(t, k, v):
    print "Assigning %s => t[%s]" % (v, k)
    t[k] = v


def dump(t):
    print "Dumping trie:"
    for k in t.keys():
        print "  t[%s] => %s" % (k, t[k])


"""  Real Samples Start Here """

print "\nUsing a simple string as keys and numeric values..."
t = Trie()
assign(t, 'string1', 1)
assign(t, 'string2', 2)
dump(t)

print "\nUsing lists as keys and bool values..."
t = Trie()
assign(t, [1, 2], True)
assign(t, [2, 3], False)
dump(t)

print "\nUsing mixed types as keys and values..."
t = Trie()
assign(t, [1, 2], 'Hello?')
assign(t, 'World', 'Earth')
assign(t, 'Planet Number', 3)
assign(t, (2, 1), 'X')
dump(t)
