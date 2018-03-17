from scipy.integrate import odeint
import numpy as np
from numpy import sin, cos
import matplotlib.pyplot as plt
import matplotlib.animation as animation
 # these are our constants
k = -2.5 # Newtons per metre
m = 1.5 # Kilograms
g = 9.8 # metres per second
l = 0.05
I = (1/12)*m*l

def MassSpring(state,t):
  # unpack the state vector
  th = state[0]
  th_d = state[1]

##  # these are our constants
##  k = -2.5 # Newtons per metre
##  m = 1.5 # Kilograms
##  g = 9.8 # metres per second
##  l = 0.05
##  I = (1/12)*m*l
  # compute acceleration xdd
  th_dd = m*g*sin(th)*(l/2)-0.1*th_d

  # return the two state derivatives
  return [th_d, th_dd]

state0 = [np.pi/2, 0.0]

dt = 0.05
t = np.arange(0.0, 20, dt)

state = odeint(MassSpring, state0, t)



x1 = l*sin(state[:, 0])
y1 = l*cos(state[:, 0])
x2 = l*sin(state[:, 0])
y2 = l*cos(state[:, 0])

fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on = False, xlim = (-0.1, 0.1), ylim = (-0.1, 0.1))
ax.grid()

line, = ax.plot([],[], 'o-', lw = 2)

time_template = 'time = %0.1fs'
time_text = ax.text(0.05, 0.9, '', transform = ax.transAxes)


def init():
    line.set_data([], [])
    time_text.set_text('')
    return line, time_text


def animate(i):
    thisx = [0, x1[i], x2[i]]
    thisy = [0, y1[i], y2[i]]

    line.set_data(thisx, thisy)
    time_text.set_text(time_template % (i*dt))
    return line, time_text

ani = animation.FuncAnimation(fig, animate, np.arange(1, len(state)),
                              interval=25, blit=True, init_func=init)

# ani.save('double_pendulum.mp4', fps=15)
plt.show()

##plt.plot(t, state)
##plt.xlabel('TIME (sec)')
##plt.ylabel('STATES')
##plt.title('Mass-Spring System')
##plt.legend(('$th$ (rad)', '$\dot{th_d}$ (rad/sec)'))
##plt.show()
