
#repeated application of the formula u[n+1] is implemented in a for-loop
#and the solution can be stored in a list or a NumPy array. 

# here we import libraries
import numpy as np
import matplotlib.pyplot as plt


def forward_euler(f, u0, T, N):
    """Solve u’=f(t, u), u(0)=u0, with n steps until t=T."""
    t = np.zeros(N + 1)
    u = np.zeros(N + 1) # u[n] is the solution at time t[n]
    u[0] = u0
    dt = T / N
    for n in range(N):
        t[n + 1] = t[n] + dt
        u[n + 1] = u[n] + dt * f(t[n], u[n])
    return t, u

def f(t, u):
    return u

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

plt.plot(t, u, label = "N=exp(x)")
plt.plot(t_2, u_2, label = "N=20", linestyle="", marker="+") 
plt.plot(t_3, u_3, label = "N=10", linestyle="", marker="+") 
plt.legend() 
plt.title("Simple line plot")
plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.show()