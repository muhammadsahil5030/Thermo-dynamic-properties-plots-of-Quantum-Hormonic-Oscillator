#____________________________"IMPORTING MODULES"____________________________________

from math import*
from numpy import*
from matplotlib import pyplot as plt

#____________________________"THERMODYNAMIC PROPERTIES OF QHO"______________________

T=linspace(0,10,1000)
N=1

def partition_function(T):
    z=exp(-1/T)/(1-exp(-1/T))
    return z

def average_energy(T):
    ave_energy=(1/2)+(exp(-1/T)/(1-exp(-1/T)))
    return ave_energy

def entropy(T):
    s=-log(1-(exp(-1/T)))+(1/T)*(exp(-1/T)/(1-exp(-1/T)))
    return s

def heat_capacity(T):
    Cv=-1*(-N/T**2)*((1-exp(-1/T))*(exp(-1/T))+exp(-2/T)/((1-exp(-1/T))**2))
    return Cv
#___________________________"PLOTTING ALL THE DEFINED FUNCTIONS"___________________

plt.plot(T, partition_function(T))
plt.plot(T, average_energy(T))
plt.plot(T, entropy(T))
plt.plot(T, heat_capacity(T))

plt.xlabel("Temperature")
plt.ylabel("Z, <E>, S, Cv")
plt.legend(["Z(T)","<E>","S(T)", "Cv"])
plt.xlim(0,3.5)
plt.ylim(-1,3.5)
plt.grid()
plt.show()
#_____________________________________END____________________________________________
