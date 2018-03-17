import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# prepare some coordinates
x, y, z = np.indices((5, 5, 5))

# draw cuboids in the top left and bottom right corners, and a link between them
cube1 = (x < 0.9) & (y < 0.9) & (z < 0.9)
#cube2 = (6 >= x >= 7) & (6 >= y >= 7) & (6 >= z >= 7)
link = abs(x - 3) + abs(y - 3) + abs(z) <= 0.5

# combine the objects into a single boolean array
voxels = cube1 | link #cube2 #| link

# set the colors of each object
colors = np.empty(voxels.shape, dtype=object)
colors[link] = 'red'
colors[cube1] = 'blue'
#colors[cube2] = 'green'

# and plot everything
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.voxels(voxels, facecolors=colors, edgecolor='k')

plt.show()
