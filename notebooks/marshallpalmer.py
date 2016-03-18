import numpy as np
from matplotlib import pyplot as plt
plt.style.use('ggplot')
D=np.arange(0,5,0.1)
Dmm=D
Dcm=D*0.1
N0=0.08*1.e6*1.e-1 #m**{-3} mm^{-1}
R=1.
theLambda=41*R**(-0.21)
curve1=N0*np.exp(-theLambda*Dcm)
R=5.
theLambda=41*R**(-0.21)
curve2=N0*np.exp(-theLambda*Dcm)
R=25.
theLambda=41*R**(-0.21)
curve3=N0*np.exp(-theLambda*Dcm)
fig, ax = plt.subplots(1,1,figsize=(10,8))
ax.semilogy(D,curve1,label='1 mm/hr')
ax.semilogy(D,curve2,'r-',label='5 mm/hr')
ax.semilogy(D,curve3,'g-',label='25 mm/hr')
ax.set_xlabel('Drop diameter (mm)')
ax.set_ylabel('$n(D) m^{-3} mm^{-1}$')
ax.set_title('Marshall Palmer distribution for three rain rates')
ax.legend(loc='best')

#Thompkins pg. 81
#to use diff must omit lasat value of Dcm

Dint = (np.sum(Dcm[:-1]*N0*np.exp(-theLambda*Dcm[:-1])*np.diff(Dcm[:-1])))\
/(np.sum(N0*np.exp(-theLambda*Dcm[:-1])*np.diff(Dcm[:-1]))


diameter = np.array([0,50,1000,5000])/1000000 #m
radius = diameter/2

rho = 1  #kg/m^3
rholiq = 1000 #kg/m^3
R = 15 #mm/hr
g = 9.81  #m/s^2
W1 = 1.2e8*radius**2
W2 = -np.sqrt(rholiq/rho*g*D)
