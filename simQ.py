def simQ(q, emission_states, duration_s, frame_rate_hz):
    """Simulate kinetic trajectory following specified
       author: David S. White
       contact:  dswhite2012@gmail.com

       updates:
       --------
       2019-08-29  DSW wrote the code
       2019-10-04 DSW  removed the np.argwhere and replaced with loop for speed increase

       Overview:
       ---------
       Generates a state_sequence over duration_s discretized to frame_rate_hz
       from the provided Q matrix and with assignments to emission_states

       Input Variables
       ---------------
       Q = [k,k] matrix where k is the total number of simulated states
       and Q(i,j) is the transition rate from state i to state j

       emission_states = state assignments for each state in Q.

       duration_s = total time (s) of data points to simulate

       frame_rate_hz = frame rate to discretize to

       Output variables:
       -----------------
       stateSequence = column vector of [n_data_points,1] simulation from Q matrix.

"""
    # import stuff

    import numpy as np

    # need to do assertions...

    # find the number of states
    n_states = np.shape(q)[1]

    #  find total time of the trajectory
    duration_f = duration_s * frame_rate_hz

    #  convert Q to frame rate
    q = q - np.diag(np.sum(q, 1))
    s = np.append(q, np.ones((n_states, 1)), axis=1)
    # multiple self by transpose
    s = np.matmul(s, s.T)
    # state probabilities are the sum of the inverse of s
    p0 = np.sum(np.linalg.inv(s), axis=0)

    # convert q matrix to rates discretized at frame rate
    A = 1 - np.exp(np.divide(-q, frame_rate_hz))

    # remove transitions from self to self and normalize
    for j in range(0, n_states):
        A[j, j] = 0
        A[j, j] = 1 - np.sum(A[j, :])

    # allocate an empty state sequence
    state_sequence = np.zeros((duration_f + 1, 1), dtype=int)
    cumsum_p0 = np.cumsum(p0)

    # determine initial state
    state = -1
    while state < 0:
        random_transition_probs = np.random.random((duration_f + 1,))
        prob_sum = np.cumsum(p0)
        for i in range(0, n_states):
            if prob_sum[i] >= random_transition_probs[0]:
                state = i
                break

        #state = np.argwhere(np.cumsum(p0) >= random_transition_probs[0])[0][0]

    # assign the first state in the state sequence (0 indexing)
    state_sequence[0] = emission_states[state]

    # finish the simulation
    for x in range(1, duration_f + 1):
        prob_sum = np.cumsum(A[state, :])
        for i in range (0, n_states):
            if prob_sum[i] >= random_transition_probs[x]:
                state = i
                break

        # state = np.argwhere(np.cumsum(A[state, :]) >= random_transition_probs[x])[0][0]
        state_sequence[x] = emission_states[state]

    return state_sequence
