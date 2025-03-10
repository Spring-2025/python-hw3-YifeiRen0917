# -*- coding: utf-8 -*-
"""Week6VaR.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17cvl6LdrQxJ6SkmfZziPFbor5IP5aPub
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def VaR(r, confidence, principal = 1):
    # This function returns the left tail value and displays a histogram
    # r = a vector of stock returns
    # principal = investment initial value
    percentile_value = np.percentile(r, (1 - confidence) * 100)
    out = principal * abs(percentile_value)
    # out = principal * positively stated value of r at the 1-alpha percentile
    return out

# Partial demonstration
def percent_var(r, confidence):
    # This function returns the left tail value and displays a histogram
    # r = a vector of stock percent returns
    # out = positively stated value of r at the 1-alpha percentile

    plt.hist(r, bins=50, alpha = 0.75)
    plt.show()

    alpha = 0.75
    out = np.percentile(r, (1 - alpha) * 100)  # Calculate the percentile
    return abs(out)  # Return the absolute value of the calculated percentile

# Unit test
r = np.random.normal(0.05, 0.03, 1000000)
probability2SD = 0.977249868  # Probability under normal curve within 2 standard deviations
percent_var = VaR(r, probability2SD)
print(np.round(percent_var, 2) == 0.01)