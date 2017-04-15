from  run_search import *
import os
import time
import signal

class TimeoutException(Exception):   # Custom exception class
    pass

def timeout_handler(signum, frame):   # Custom signal handler
    raise TimeoutException

# Change the behavior of SIGALRM
signal.signal(signal.SIGALRM, timeout_handler)

searches = [7,8,9,10] # How many strategies should we look at

problems =[1,2,3] # Which problems are we running over

time_limit = 600 # Maximum seconds to try a search

for search in searches:
    for problem in problems:
        arg1 = str(problem)
        arg2 = str(search)
        python_executable = "python run_search.py -p " +arg1+ " -s " + arg2
        print("Attempting problem {} with search strategy {}".format(arg1, arg2))

        signal.alarm(time_limit) # FIXME: Does fuck all, but at least it loops I guess. 
        try:
            os.system(python_executable)
        except TimeoutException: 
            continue # continue the for loop if function takes more than time_limit
        else:
            # Reset the alarm
            signal.alarm(0)
