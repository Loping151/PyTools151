# --------------------------------------------------------------------------------
# Author: Loping151
# GitHub: https://github.com/Loping151/pytools151
# Description: This repository contains a collection of Python tools designed to
#              enhance productivity and simplify various tasks. The code is open
#              for use and can be freely used, modified, and distributed.
# License: MIT License - Feel free to use and modify the code as you wish.
# --------------------------------------------------------------------------------
import concurrent.futures
from tqdm import tqdm

def parallel_run(func, iter_items, args, num_workers=24):
    """
    Run a function in parallel on a list of items.
    
    Args:
    func (function): The function to run. The first argument should be the item to iterate over.
    args (list): List of additional arguments to pass to the function.
    iter_items (list): List of items to iterate over.
    """
    with concurrent.futures.ProcessPoolExecutor(max_workers=num_workers) as executor:
        tasks = [executor.submit(func, item, *args) for item in iter_items]
        for _ in tqdm(concurrent.futures.as_completed(tasks), total=len(tasks)):
            pass
        
        
if __name__ == "__main__":
    import time
    import random

    def slow_function(item, sleep_time=None):
        if sleep_time is None:
            sleep_time = random.randint(1, 3)
        print(f"Processing {item}...")
        time.sleep(sleep_time)
        print(f"Done processing {item} after {sleep_time} seconds.")

    items = list(range(10))
    parallel_run(slow_function, items, [])