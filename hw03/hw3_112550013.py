#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sample code of HW3 Problem 5
Monte Carlo estimate of the Euler Number
"""
import numpy as np
from tqdm import tqdm

def estimate_e(N_trials):
    n_list = []

    for _ in tqdm(range(N_trials), desc=f"Running {N_trials} trials"):
        S = 0.0
        n = 0
        while S <= 1.0:
            U = np.random.uniform(0, 1)
            S += U
            n += 1
        n_list.append(n)

    euler_number_est = np.mean(n_list)
    return euler_number_est, n_list

if __name__ == "__main__":
    trial_numbers = [10**1, 10**3, 10**5, 10**7]
    estimates = {}

    for N in trial_numbers:
        print(f"\nEstimating e with {N} trials:")
        e_estimate, _ = estimate_e(N)
        estimates[N] = e_estimate
        print(f"Estimated e: {e_estimate}")

    print("\nAll Estimates of Euler's Number e:")
    for N, est in estimates.items():
        print(f"Trials: {N:>8}, Estimated e: {est:.10f}")