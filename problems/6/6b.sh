#! /bin/bash

# count the number of lines in each python file in the current directory and
# all subdirectories

# By default xargs uses -n of 5000, so there will be a count every 5k lines if there are very many files so we strip line count totals with grep (this could be removed if the totals are desirable)
find ./ -type f -name "*.py" -print0 | xargs -0 wc -l | grep -Ev "[ ]+ [0-9]+ total$"
