import math
import os
import re
import sys
from collections import Counter, OrderedDict, defaultdict, deque, namedtuple
from datetime import datetime
from functools import lru_cache, reduce
from itertools import chain, combinations, permutations, product

import numpy as np
from tqdm import tqdm

cur_dir = os.path.dirname(os.path.abspath(__file__))
par_dir = os.path.dirname(cur_dir)
sys.path.append(par_dir)

from util.general_util import load_input, timer

last_dir = str(os.path.basename(os.path.normpath(cur_dir)))
cur_day = re.findall(r"\d+", last_dir)
cur_day = int(cur_day[0]) if len(cur_day) > 0 else datetime.today().day
images_path = os.path.join(par_dir, "images")


def build_diff(values):
    return [values[i + 1] - values[i] for i in range(len(values) - 1)]


def extrapolate(hist_steps, last_value):
    return hist_steps[-1] + last_value


@timer(return_time=True)
def task1(day_input):
    day_input = day_input.splitlines()
    for hist in day_input:
        hist = [int(v) for v in hist.split()]
        hist_steps = [hist] + [build_diff(hist)]
        while not all([v == 0 for v in hist_steps[-1]]):
            hist_steps.append(build_diff(hist_steps[-1]))
        hist_steps[-1].append(0)
        print(f"Lenght: {len(hist_steps)}")
        for i in range(len(hist_steps) - 2, -1, -1):
            hist_steps[i].append(extrapolate(hist_steps[i], hist_steps[i + 1][-1]))

        print(hist_steps)

        break


@timer(return_time=True)
def task2(day_input):
    # Day-specific code for Task 2
    pass


def main():
    # Choose between the real input or the example input
    # day_input = load_input(os.path.join(cur_dir, "input.txt"))
    day_input = load_input(os.path.join(cur_dir, "example_input.txt"))

    # Call the tasks and store their results (if needed)
    result_task1, time_task1 = task1(day_input)
    result_task2, time_task2 = task2(day_input)

    print(f"\nDay {cur_day}")
    print("------------------")
    # Print the results
    print("\nAnswers:")
    print(f"Task 1: {result_task1}")
    print(f"Task 2: {result_task2}")

    print("\nTimes:")
    print(f"Task 1: {time_task1:.6f} seconds")
    print(f"Task 2: {time_task2:.6f} seconds")


if __name__ == "__main__":
    main()
