import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import scipy.integrate as integr

g = 9.81
L = 0.1
frot = 0.3

dt = 0.01
pulse = 2 * np.pi / np.sqrt(g/L)
anim_duration = 1000*pulse

pos_init = np.pi/3
vit_init = 0

def f(theta, t):
	return np.array([theta[1], -frot * theta[1] - g/L * np.sin(theta[0])])

T = np.arange(0, anim_duration, dt)
thetas = integr.odeint(f, np.array([pos_init, vit_init]), T)


fig, (graph, pendule) = plt.subplots(1, 2)
graph.set_xlabel("Time [s]")
graph.set_ylabel("Angle [rad]")
graph.set_xlim(0, 10)
graph.plot(T, thetas[:, 0])

pendule.set_xlim(-L, L)
pendule.set_ylim(-L, L)
plt.axis('off')
line, = pendule.plot([],[],c='r')
masse = pendule.scatter([],[],c='r')
def animate(i):
	theta = thetas[:, 0][i]
	x = L*np.sin(theta)
	y = -L*np.cos(theta)

	line.set_data([0, x], [0, y])
	masse.set_offsets([x, y])
	return line,masse,

ani = animation.FuncAnimation(fig, animate, frames = int(anim_duration/dt), interval=dt)

plt.show()
