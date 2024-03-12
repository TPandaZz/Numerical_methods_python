# -*- coding: utf-8 -*-
"""
Created on Mar 9

@author: Michal Sleszynski

Learning about Logistic growth that can be used to model self-limiting growth 
of a biological population 

for such model we have growth rate alpha, and the carrying capacity R

need (__init__) which takes an argument RHS function f and stores it 
as an attribute

set_initial_condition takes the initial condition as argument and stores it

solve-method takes the time interval t_span and number of time steps N
method implements the for-loop for solving the ODE and returns the solution

time step dt and the sequences t_n, u_n are initialized in one of the
methods

Credit: Joakim Sundnes "Solving Ordinary Differential Equations in Python"
"""

import numpy as np
import matplotlib.pyplot as plt

class ForwardEuler_v0:
    def __init__(self, f):
        self.f = f
    
    def set_initial_condition(self, u0):
        self.u0 = u0
    
    def solve(self, t_span, N):
        t0, T = t_span
        self.dt = T / N
        self.t = np.zeros(N + 1) 
        self.u = np.zeros(N + 1)
        self.t[0] = t0
        self.u[0] = self.u0
        
        for n in range(N):
            self.n = n
            self.t[n + 1] = self.t[n] + self.dt
            self.u[n + 1] = self.advance()
        return self.t, self.u
    
    def advance(self):
        # Advance the solution one time step
        # Create local variables to get rid of self. 
        u, dt, f, n, t = self.u, self.dt, self.f, self.n, self.t
        
        return u[n] + dt * f(t[n], u[n])

# implement the function as a class with a call method
class Logistic:
    def __init__(self, alpha, R):
        self.alpha, self.R = alpha, float(R)
    def __call__(self, t, u):
        return self.alpha * u * (1 - u / self.R)

# Define parameters for the ODE
alpha=0.15 # Growth rate
R=60.0 # Carrying Capacity
u0 = 0.1 # Initial condition
T = 80 # Time

problem = Logistic(alpha, R)
solver = ForwardEuler_v0(problem)
solver.set_initial_condition(u0)
t, u = solver.solve(t_span=(0, T), N=1000)

# Plotting the solution
plt.plot(t,u, label = "Logistic Growth") 
plt.axhline(y = R, color = 'r', linestyle = '--', label = "Carrying Capacity") 
plt.legend() 
plt.title("Solution for Simple ODE")
plt.xlabel("Time")
plt.ylabel("Population Size")
plt.show()