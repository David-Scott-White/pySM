import numpy as np
import matplotlib.pyplot as plt
from simQ import simQ
from addNoise import addNoise
import time

q = np.array([[0., 0.1], [0.2, 0.]])
emission_states = list(range(1, 4))
duration_s = 1000
frame_rate_hz = 10

t1 = time.time()
state_sequence = simQ(q, emission_states, duration_s, frame_rate_hz)
state_sequence = addNoise(state_sequence, [100, 200], 'Gaussian', 19)
t2 = time.time()
print(t2-t1)

plt.figure()
plt.plot(state_sequence[1], label='added noise')
plt.plot(state_sequence[0], label='true sequence')
plt.legend(loc='upper right')
plt.xlabel('Time (s)')
plt.ylabel('Intensity (au)')
plt.show()
