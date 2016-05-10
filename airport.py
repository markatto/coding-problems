#! /usr/bin/env python3
import sys
filename = sys.argv[1]

with open(filename, 'r') as f:
    traveller_count, worker_count = [int(s) for s in f.readline().strip().split(' ')]

    worker_minutes_required = [int(minutes) for minutes in f.readline().strip().split(' ')]
    # initialize minutes_spent to minutes_required to simplify loop
    workers = [{'minutes_required': minutes, 'minutes_spent': minutes} for minutes in worker_minutes_required]

    time_spent = 0
    line_pos = 0
    # step through minutes
    while True:
        time_spent += 1
        # step through workers
        for worker_index,worker in enumerate(workers):

            # if worker is done, give them a new traveller
            if worker['minutes_spent'] >= worker['minutes_required']:
                worker['minutes_spent'] = 1
                line_pos += 1
                # check if we're the one being processed
                if line_pos == traveller_count:
                    print('%d %d' % (time_spent, worker_index))
                    sys.exit(0)

            # otherwise, do a minute of work
            else:
                worker['minutes_spent'] += 1
            print(workers)



# output: "time_taken last_worker_used"

