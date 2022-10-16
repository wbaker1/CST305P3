#CST-305 Project 3 - Matthew Powers and Wesley Baker 
#This project is a graph of the second-order differential equations yh(x) and y(x) solution
#The equations are y''+2y'+y = 2x and y'' + y = x^2 using Green's Function, Undetermined Coefficients and Variation of Parameters


import numpy as np
import matplotlib.pyplot as plt


# time points
t = np.linspace(0,7,1000)

def greens_function_result_1(t):
    return 2*t*np.exp(-t) + 4*np.exp(-t) + 2*t - 4

def homogeneous_function_result_1(t):
    return 2*t*np.exp(-t) + 4*np.exp(-t)

def greens_function_result_2(t):
    return  t**2 + 2*np.cos(t) - 2

def homogeneous_function_result_2(t):
    return 2*np.cos(t)

#################################################################
# plot results for greens function problem 1
plt.plot(t,greens_function_result_1(t),'b-', label='Greens Function line')

# label neccessary info on graph
plt.title('Greens Function Graph For Problem 1')
plt.xlabel('x val')
plt.ylabel('y val')
plt.legend()
# Display the graph
plt.show()
#################################################################

#################################################################
# plot results for Homogeneous function probelm 1
plt.plot(t,homogeneous_function_result_1(t),'b-', label='Homogeneous Function line')

# label neccessary info on graph
plt.title('Homogeneous Graph For Problem 1')
plt.xlabel('x val')
plt.ylabel('y val')
plt.legend()
# Display the graph
plt.show()
#################################################################

#################################################################
# plot results for greens function probelm 2
plt.plot(t,greens_function_result_2(t),'b-', label='Greens Function line')

# label neccessary info on graph
plt.title('Greens Function Graph For Problem 2')
plt.xlabel('x val')
plt.ylabel('y val')
plt.legend()
# Display the graph
plt.show()
#################################################################

#################################################################
# plot results for Homogeneous function probelm 2
plt.plot(t,homogeneous_function_result_2(t),'b-', label='Homogeneous Function line')

# label neccessary info on graph
plt.title('Homogeneous Graph For Problem 2')
plt.xlabel('x val')
plt.ylabel('y val')
plt.legend()
# Display the graph
plt.show()
#################################################################
