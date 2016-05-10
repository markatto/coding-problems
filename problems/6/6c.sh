#! /bin/bash

# Count the number of lines in each python file in the current directory
# and all subdirectories and print a total "even if there are many many files,"
# My solutions for 6a and 6b actually print totals, but they won't work
# if there's too many files to fit in the argument list for a single call to
# `wc`, so we'll address that here.

# this takes ~2m47s on a directory with 100k 4-line files on an SSD
#find ./ -type f -name "*.py" -print0 | xargs -0 -n 1 wc -l | awk '{ total+=$1} END {print total}'

# we make fewer wc calls to be faster here
# using the same directory and SSD, this takes ~1s with cache warm
find ./ -type f -name "*.py" -print0 | xargs -0 -n 2000 wc -l | \
grep -Ev "^[ ]+ [0-9]+ total$" | awk '{ total+=$1} END {print total}'


# Using GNU parallel like this could make it faster for some workloads
# and/or hardware (NVM-E SSDs that like a high queue depth come to mind),
# but it's slower for my mostly-cached test workload. Using xargs with --parallel
# is faster and does increase speed, but it can give inaccurate results
# when output gets intermingled.
#find ./ -type f -name "*.py" -print0 | parallel --xargs -q0 -j5 wc -l | \
#grep -Ev "^[ ]+ [0-9]+ total$" | awk '{ total+=$1} END {print total}'
