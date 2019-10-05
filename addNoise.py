def addNoise(state_sequence, state_values, noise_type, noise_parameters):
    """Add noise to a simulated trajectory
       author: David S. White
       contact: dswhite2012@gmail.com

       updates:
       --------
       2019-10-04 DSW started writing the code [only works for Gaussian noise right now]

       Overview:
       ---------
       Add noise to trajectories simulated with simQ.py.
       Noise options will include:
          *  Gaussian
          *  Poisson
          *  Poisson-Gamma-Normal [PGN]

       Input Variables
       ---------------
        state_sequence = sequence of discrete states in numpy array

        state_values = assignment of discrete states [i.e. 1, 2, ...] into observed values [i.e. 100, 200, ...]

        noise_type = string of type of noise to add to the trajectory

        noise_parameters = i.e. mu and sd of gaussian, lambda of poisson, more complicated for PGN...

       Output variables:
       -----------------
       state_sequence_noise = column vector of [n_data_points,1] with added noise

        """

    import numpy as np

    # find the number of states
    n_data_points = len(state_sequence)

    # grab the initial state values
    initial_states = np.unique(state_sequence)

    # duplicate state_sequence for to modify
    true_sequence = state_sequence

    # replace the initial state values with the new values
    for i in range(0,len(initial_states)):
        true_sequence[state_sequence == initial_states[i]] = state_values[i]

    # now add the noise directly
    if noise_type == 'Gaussian':
        state_sequence_noise = np.random.normal(true_sequence, noise_parameters)

    elif noise_type == 'Poisson':
        state_sequence_noise = np.random.poisson(true_sequence)

    return  (true_sequence , state_sequence_noise)

