import numpy as np
import matplotlib.pyplot as plt
from theory import FrictionPendulum

conv = 180 / np.pi

pen = FrictionPendulum(0.3, 0.64e-2, 24.5e-2, 66.0e-2, 15)

t = np.arange(1052) * 0.01
theta = []
omega = []
for i in t:
	theta.append(pen.theta(i))
	omega.append(pen.omega(i))
theta = np.array(theta)
omega = np.array(omega)

# Drawing plots:

fig = plt.figure()
gr = fig.add_subplot(111)
gr.plot(t,theta)
gr.plot(t,t*0,'k--')
plt.savefig('theta.png')

plt.clf()

fig = plt.figure()
gr = fig.add_subplot(111)
gr.plot(t,omega)
gr.plot(t,t*0,'k--')
plt.savefig('omega.png')
