import numpy as np
import matplotlib.pyplot as plt

theta=np.random.uniform(0.0,np.pi/2.0,1000000) 
vel=np.random.uniform(35.0,45.0,1000000) 
d=(vel**2.0)*np.sin(2.0*theta)/9.8
v1=vel[np.logical_and(d>56.0,d<66.0)]
v2=vel[np.logical_and(d>110.0,d<120.0)]
v3=vel[np.logical_and(d>27.0,d<37.0)]
v4=vel[np.logical_and(d>172.0,d<182.0)]

plt.hist(vel,100,normed=1)
plt.hist(v1,100,normed=1)
plt.hist(v2,100,normed=1)
plt.hist(v3,100,normed=1)
plt.hist(v4,100,normed=1)


plt.title('Alcance',fontsize=25)
plt.xlabel('velocidad',fontsize=25)
plt.ylabel('prob.velocidad',fontsize=25)
plt.show()
plt.savefig('Alcance.png')
plt.close()



