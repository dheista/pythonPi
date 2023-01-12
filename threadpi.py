#!/usr/bin/env python3

import argparse
import math
import threading

def calc_pi(start: int, end: int) -> float:
    numerator: float = 4.0
    denominator: float = start * 2 + 1
    operation: float = 1.0 if start % 2 == 0 else -1.0
    pi: float = 0.0
    for i in range(start, end):
        pi += operation * (numerator / denominator)
        denominator += 2.0
        operation *= -1.0
    return pi

if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--n_terms", type=int, default=100000, help="Number of terms to use in the calculation of pi")
    parser.add_argument("--n_threads", type=int, default=4, help="Number of threads to use in the calculation")
    args = parser.parse_args()

    # Calculate pi using multiple threads
    terms_per_thread = args.n_terms // args.n_threads
    threads = []
    for i in range(args.n_threads):
        start = i * terms_per_thread
        end = (i + 1) * terms_per_thread
        thread = threading.Thread(target=calc_pi, args=(start, end))
        thread.start()
        threads.append(thread)

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    # Calculate and print the final value of pi
    pi = sum(thread.result for thread in threads)
    print(pi)
