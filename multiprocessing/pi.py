# for loop
import os
import random
import time
from multiprocessing import Pool

def estimate_nbr_points_in_quarter_circle(nbr_estimates):
    """
    使用純 Python,以 Monte Carlo 法估計四分之一圓內的點數
    """
    print(f"Executing estimate_nbr_points_in_quarter_circle \
          with {nbr_estimates:,} on pid {os.getpid()}")
    
    nbr_trials_in_quarter_unit_circle = 0
    for step in range(int(nbr_estimates)):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        is_in_unit_circle = x * x + y * y <= 1.0
        nbr_trials_in_quarter_unit_circle += is_in_unit_circle

    return nbr_trials_in_quarter_unit_circle

if __name__ == "__main__":
    nbr_samples_in_total = 1e8
    nbr_parallel_blocks = 4
    nbr_samples_per_worker = nbr_samples_in_total / nbr_parallel_blocks
    
    pool = Pool(processes=nbr_parallel_blocks)

    print("Making {:,} sample per {} worker".format(nbr_samples_per_worker, nbr_parallel_blocks))

    nbr_samples_per_process = [nbr_samples_per_worker] * nbr_parallel_blocks

    t1 = time.time()
    nbr_in_quater_unit_circles = pool.map(estimate_nbr_points_in_quarter_circle,
                                          nbr_samples_per_process)
    
    print("the number of samples in quater unit circles in each process: ", nbr_in_quater_unit_circles)

    # PI = 4 * c / n
    pi_estimate = sum(nbr_in_quater_unit_circles) * 4 / float(nbr_samples_in_total)
    print("Estimated pi", pi_estimate)
    print("Delta:", time.time() - t1)


