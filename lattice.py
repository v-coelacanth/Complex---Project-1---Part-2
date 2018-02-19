import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import csv
import math
import time
import pickle

""" This program was written by Vanessa Job for CS523, February 2018.   It
    builds figure 3 from the Walker paper, 'Evolutionary Transitions and
    Top-Down Causation'.  """

""" We will have N=1000 logistic maps with carrying capacity K = 100.
    We will run for time_steps = 10000 time steps.
    We compute the return map for this time series for a variety of compling
    strenths epsilon.

    Note:  There is quite a bit of dependence on initial conditions.   """

def compute_f(x_val, r_val, K):
    """ Compute the local dynamics of each element at time step n.  Return f(x_i_n).  Here r_i is
        the reproductive fitness of population i and K is the carrying capacity. """
    f = r_val * x_val * (1 - x_val/K)
    return f


def compute_big_M(n, x, N):
    """ Compute M_n = (1/N) sum{j=1 to N}(x[j,n]), a.k.a., the sum of the
        nth row of x.  """
    M = 0
    """ VANESSA, THERE HAS TO BE A BETTER WAY TO DO THIS. """
    for j in range(1, N+1):
        M = M + x[j,n]

    M = M/N

    return M


def compute_little_m(x, n, N, r, K):

    little_m = 0
    for j in range(1,N+1):
        little_m = little_m + r[j] * x[j,n] * (1 - x[j,n]/K)

    little_m = (1/N) * little_m


    return little_m


def compute_r(N):
    """
    Generate an array of fitness values for the populations. Note, we have N populations.
    The r values must be from the interval [3.9,4].
    """
    """ Note: There is no zeroth organism, so we're going to ignore r[0].
        Next time use a pandas series which is analogous to a one dim numpy
        array. """
    r = np.random.rand(N+1)
    r = 4 - r/10

    return r

def round_data(x):
    """ Return the array which consists of every element of x rounded
        to the nearest int.  """

    y = np.around(x)
    y = y.astype(int)
    return y


def compute_x (time_steps, N, epsilon, r, K, use_user_x, user_x):
    """
    r - is an array of N random fitness values for each of the populations.
        The r values must be from the interval [3.9, 4].
    epsilon - the global coupling strength.  0 <= epsilon <= 1
    K - the carrying capacity. For our example, K = 100

    """

    """ Get random r values.  """
    """ Set up initial conditions for x. """
    """ Need N rows and n+1 columns.  Row indices are from 1,2, ..., N.  Column
        indices go are from 0, 1, ..., time_steps.  """

    """ Has column labels 0..time_steps.   """
    """ Each row is a different organism. The row labels are 1..N.   We're
        ignoring row 0 because there is no organism 0. """
    x = np.zeros((N+1, time_steps+1))

    """ Set initial population size to 1.  This is column zero of x. """
    x[:,0] =1

    big_M = np.zeros(time_steps+1)
    """ n is the time step, i is organism """
    for n in range(0, time_steps):
        big_M[n] = compute_big_M(n, x, N)
        little_m_n = compute_little_m(x, n, N, r, K)

        for i in range(1, N+1):
            f = r[i] * x[i,n] * (1 - x[i,n]/K)
            x[i,n+1] = (1 - epsilon) * f + epsilon * little_m_n

    """ We will return x and big_M.  """

    return x,big_M

if __name__ == "__main__":
    t0 = time.time()
    generate_data_for_transfer_entropy = False
    generate_return_map = True
    N = 1000  # Number of populations.
    time_steps = 10000
    K = 100  # Carrying capacity.

    """ Compute r, the vector of random population fitnesses. """
    r = compute_r(N)
    if generate_data_for_transfer_entropy:
        """ Pick a random population.  """
        rand_pop = random.randrange(1, N)
        print ("Random population is population ", rand_pop, "with r value",
               r[rand_pop])
        # for e in np.arange(0.0, 1.0, 0.1):
        for e in [0.3]:
            print ("Running single population with epsilon", e)
            x, M = compute_x(time_steps, N, e, r, K, False, False)
            print ("max x, max M", np.amax(x[rand_pop, 1:len(M)-1]),
                   np.amax(M[1:len(M)]))
            print("min x, min M", np.amin(x[rand_pop, 1:len(M)-1]),
                  np.amin(M[1:len(M)]))

            """ Write out x[rand_pop] and M to files.  """
            # print ("size of x[rand_pop, 1:] is", len(x[rand_pop, 1:]))
            # print ("size of M[1:] is", len(M[1:]))
            filename = "./output/x_M_with_e" + str(e) + "_r"+str(r[rand_pop])
            with open(filename, 'w') as f:
                writer = csv.writer(f)
                for i in range(1, len(M)):
                    thing = [x[rand_pop, i], M[i]]
                    writer.writerow(thing)
                    #np.savetxt("./output/x_with_eps"+str(e), x[rand_pop, 1:])
                    #np.savetxt("./output/M_with_eps"+str(e), M[1:])

            del x
            del M
    if generate_return_map:
        """ Note: Instead of stars, we have orchid. """
        colors = ['magenta', 'red', 'blue', 'orange', 'aqua', 'darkgreen',
                 'chartreuse','black']
        epsilons = [0, 0.075, 0.1, 0.2, 0.225, 0.25, 0.3, 0.4]
        # colors = ['orchid']
        # epsilons = [0.3]
        for i in range(0,len(epsilons)):
            x, M = compute_x(time_steps, N, epsilons[i], r, K, False, False)

            """ SAVE Whatever organism we need here.  Then delete the space. """
            print("Now running epsilon", epsilons[i], "color is", colors[i])
            del x

            """ Plot return map for this epsilon.  """
            """ M goes from 0 to time_steps """
            plt.scatter(M[0:time_steps], M[1:time_steps+1], s=0.02, color=colors[i],
                        marker='.')
                        # , label = r"\epsilon = " + str(epsilons[i]))
            # plt.legend()
            """ For epsilon = 0.3, the star case in the Walker paper, most
                data oscillates between two values at the end. This is hard to
                see, so Walker et al represent this as stars in their graph.
                Figure out what those positions are and put stars at those
                positions in our graph. """

            if epsilons[i] == 0.3:
                print(" Finding max and min for epsilon = 0.3")
                start = math.floor( len(M) * 0.9)
                stop = len(M)-3
                val1 = np.amax(M[start:stop])
                val2 = np.amin(M[start:stop])
                print("Val1, val2", val1, val2)
                plt.scatter([val1, val2], [val2, val1], marker='*',
                            color = 'black', s=45)
        """ Add line y=x. """
        plt.plot(range(0,100), range(0,100), color='black', linewidth = '0.25')
        """ Put labels on the axes. """
        plt.xlabel(r"$M_n$")
        plt.ylabel(r"$M_{n+1}$")
        t1 = time.time()

        print("Total time: ", t1-t0)
        # fig = plt.figure()
        # fig.show()

        plt.xlim((35, 85))
        plt.ylim((35, 85))

        plt.show()
