# -*- coding: utf-8 -*-
"""
Created on Feb 25

@author: Michal Sleszynski

We are approximating the solution to an
initial value problem between 0 and 4 
in increments of 0.1 using the 
Explicity Euler Formula (Method to Solve ODE's)
"""

import numpy as np
import matplotlib.pyplot as plt

# Define parameters
f = lambda t, s: np.exp(t) # ODE
h = 0.1 # Step size (increase for better result)
t = np.arange(0, 4 + h, h) # Numerical grid
n0 = 1 # Initial Condition

# Explicit Euler Method
n = np.zeros(len(t))
n[0] = n0

for i in range(0, len(t) - 1):
    n[i + 1] = n[i] + h*f(t[i], n[i])


# Ploting the difference between the approximate
# solution and the exact solution
plt.figure(figsize = (12, 7))
plt.plot(t, n, 'r--', label='Approximate')
plt.plot(t, np.exp(t), 'b', label='Exact')
plt.title('Approximate and Exact Solution for Simple ODE')
plt.xlabel('t')
plt.ylabel('f(t)')
plt.legend(loc='lower right')
plt.show()