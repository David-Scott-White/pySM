import numpy as np
import matplotlib.pyplot as plt
from simulateTrajectory import simulateQ
import time

q = np.array([[0., 0., 0.1], [0.2, 0., 0.2], [0., 0.3, 0.]])
emission_states = list(range(1, 4))
duration_s = 100
frame_rate_hz = 10

t1 = time.time()
state_sequence = simulateQ(q, emission_states, duration_s, frame_rate_hz)
t2 = time.time()
print(t2-t1)

plt.figure()
plt.plot(state_sequence)
plt.show()