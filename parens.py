#! /usr/bin/env python3
import sys

with open('parens.txt') as f:
    txt = (f.read())

unclosed = []
for index, char in enumerate(txt):
    if char == '(':
        unclosed.append(index)
    if char == ')':
        if len(unclosed) < 1:
            print('FAIL: unmatched closing paren at position %d' % index)
            sys.exit(1)
        unclosed.pop()
if len(unclosed) != 0:
    print('FAIL: unmatched opening parens at the following indexes: %s' % unclosed)
    sys.exit(1)
