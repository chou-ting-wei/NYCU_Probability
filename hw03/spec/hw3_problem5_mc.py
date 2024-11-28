#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sample code of HW3 Problem 5
Monte Carlo estimate of the Euler Number
"""
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from tqdm import tqdm

# Basic parameters
# N: number of 
N_trials = 1000
n_list = []

#-------- Your code (~10 lines) ----------


#---------- End of your code -----------
# Optional: Print the Monte-Carlo estimates abnd visualize the empirical CDF
print(euler_number_est)
print(n_list)
res = stats.ecdf(np.array(n_list))
ax = plt.subplot()
res.cdf.plot(ax)
ax.set_xlabel('Estimated Euler Number')
ax.set_ylabel('Empirical CDF')
plt.show()