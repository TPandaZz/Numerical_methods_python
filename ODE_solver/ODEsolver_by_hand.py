'''
 Created on Feb 17

 @author: Michal Sleszynski
 
 Reference: Joakim Sundnes - Solving Ordinary Differential Equations in Python
 
 Implementing Forward Euler method / Explicit Euler Method
 steps:
    1. Create arrays t and u of length N + 1
    2. Set initial condition: u[0] = u0, t[0] = 0
    3. Compute the time step ∆t dt = T/N
    4. For n = 0,1,2,...,N −1:
        t[n + 1] = t[n] + dt
        u[n + 1] = (1 + dt) * u[n]
    5. to implement general solver adjust u[n+1] -
        replace u[n] with the more general f(t[n],u[n])
        
 Using this function, we can solve any kind of linear or nonlinear ODE
    1. Identify f(t,u) in the ODE
    2. Find initial condition u_0
    3. Implement the f(t,u) formula in a function f(t, u)
    4. Choose the number of time steps N
    5. Call t, u = forward_euler(f, u0, T, N)
    6. Plot the solution
'''

# import libraries
import numpy as np
import matplotlib.pyplot as plt

# define function
# Solve u’=f(t, u), u(0)=u0, with n steps until t=T
def forward_euler(f, u0, T, N):
    # create arrays
    t = np.zeros(N + 1)
    u = np.zeros(N + 1) 
    u[0] = u0
    dt = T / N
    # note u_n denote the numerical approximation to the exact solution u(t) at t_n
    for n in range(N):
        t[n + 1] = t[n] + dt
        u[n + 1] = u[n] + dt * f(t[n], u[n])
    return t, u

# f(t,u) needs to be implemented as a Python function,
# which is then passed as an argument to forward_euler 
def f(t, u):
    return u


# reducing the time step will get the solution closer to the exact solution
u0 = 1
T = 4
N = 100000
t, u = forward_euler(f, u0, T, N)

u0_2 = 1
T_2 = 4
N_2 = 20
t_2, u_2 = forward_euler(f, u0_2, T_2, N_2)

u0_3 = 1
T_3 = 4
N_3 = 10
t_3, u_3 = forward_euler(f, u0_3, T_3, N_3)

plt.plot(t, u, label = "Exact solution exp^x")
plt.plot(t_2, u_2, label = "Forward Euler, t = 0.2", linestyle="", marker="+") 
plt.plot(t_3, u_3, label = "Forward Euler, t = 0.4", linestyle="", marker="+") 
plt.legend() 
plt.title("Simple line plot")
plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.show()