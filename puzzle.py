#! /usr/bin/env python3
import sys
filename = sys.argv[1]
with open(filename, 'r') as f:
    spec = f.readline().strip().split(' ')
    puzzle_size = int(spec[0])
    word_count = int(spec[1])

    puzzle = []
    puzzle_words = []
    for _ in range(puzzle_size):
        puzzle.append(f.readline().strip())
    for _ in range(word_count):
        puzzle_words.append(f.readline().strip())

puzzle_words = {word: False for word in puzzle_words}

for y in range(puzzle_size):
    for x in range(puzzle_size):
        # check horizontal
        row = puzzle[y]
        # check vertical 
        column = ''.join([r[x] for r in puzzle])
        
        for word in puzzle_words.keys():
            if word in row or word in column:
                puzzle_words[word] = True

if False not in puzzle_words.values():
    print('True')
else:
    print('False')

