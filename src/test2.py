import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter
from particle_class import Particle

from equation_helpers import magnetic_force, larmor_radius


B_dir = np.array([0, 0.1, 10])  # Magnetic field direction (z-axis)
dt = 0.001

p1 = Particle(position=np.array([0, 0.0, 0.0]), velocity=np.array([15.0, 0.0, 0.0]), mass=1.0, charge=5.0)
p2 = Particle(position=np.array([0.0, 0.0, 0.0]), velocity=np.array([15.0, 0.0, 0.0]), mass=2.0, charge=5.0)
p3 = Particle(position=np.array([0.0, 0.0, 0.0]), velocity=np.array([15.0, 0.0, 0.0]), mass=3.0, charge=5.0)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.set(xlabel='X', ylabel='Y', zlabel='Z')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_zlim(-0.25, 0.25)

positions1 = [p1.position.copy()]
positions2 = [p2.position.copy()]
positions3 = [p3.position.copy()]
trajectory1, = ax.plot([], [], [], lw=2, color='blue', label='Trajectory 1')
trajectory2, = ax.plot([], [], [], lw=2, color='red', label='Trajectory 2')
trajectory3, = ax.plot([], [], [], lw=2, color='green', label='Trajectory 3')
particle_dot1, = ax.plot([], [], [], 'ro', label='Particle 1')
particle_dot2, = ax.plot([], [], [], 'ro', label='Particle 2')
particle_dot3, = ax.plot([], [], [], 'ro', label='Particle 3')

num_frames = 500
metadata = dict(title="Particle Animation", artist="Matplotlib")
writer = PillowWriter(fps=24, metadata=metadata)

with writer.saving(fig, "particleani.gif", 100):
    for i in range(num_frames):
        force = magnetic_force(p1.charge, p1.velocity, B_dir)
        acceleration = force / p1.mass

        p1.velocity += acceleration * dt
        p1.position += p1.velocity * dt

        positions1.append(p1.position.copy())

        force = magnetic_force(p2.charge, p2.velocity, B_dir)
        acceleration = force / p2.mass

        p2.velocity += acceleration * dt
        p2.position += p2.velocity * dt

        positions2.append(p2.position.copy())

        force = magnetic_force(p3.charge, p3.velocity, B_dir)
        acceleration = force / p3.mass

        p3.velocity += acceleration * dt
        p3.position += p3.velocity * dt

        positions3.append(p3.position.copy())

        points1 = np.array(positions1)
        trajectory1.set_data_3d(points1[:, 0], points1[:, 1], points1[:, 2])
        particle_dot1.set_data_3d([p1.position[0]], [p1.position[1]], [p1.position[2]])

        points2 = np.array(positions2)
        trajectory2.set_data_3d(points2[:, 0], points2[:, 1], points2[:, 2])
        particle_dot2.set_data_3d([p2.position[0]], [p2.position[1]], [p2.position[2]])

        points3 = np.array(positions3)
        trajectory3.set_data_3d(points3[:, 0], points3[:, 1], points3[:, 2])
        particle_dot3.set_data_3d([p3.position[0]], [p3.position[1]], [p3.position[2]])

        writer.grab_frame()
