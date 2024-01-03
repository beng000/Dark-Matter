
import numpy as np
from math import pi, sqrt
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
from scipy.special import zeta 
from matplotlib.axes import Axes
from scipy.integrate import quad


z = np.arange(0, 11, 0.01)

#def integrand(y,z,i):
    #np.exp((y**2)/sqrt((y**2)+z[i]**2)) + 1
    
#def integrand(y):
   # (y**2)/(np.exp(sqrt((y**2))+1))
    
    

#n = quad(integrand, 0, np.inf)


N_nonrel = ((((2**(3/2))*sqrt(pi))/(6*zeta(3)))*(z**(3/2))*np.exp(-z))
print(N_nonrel)



plt.loglog(z, N_nonrel)
plt.xlabel('z=Mx/T')
plt.ylabel('N(z>>1)')
plt.grid()
