#!/usr/bin/env python2.7

from __future__ import print_function, division

# from mpi4py import MPI
import numpy as np
import matplotlib.pyplot as plt

from mpi_util import *

if __name__ == "__main__":
    print("hey")
    nproc = 10
    data = np.random.rand(1000000)
    assigned_rank = assign_id_to_rank(data, nproc)
    split_data = split_data_by_assigned_rank(assigned_rank, assigned_rank, nproc)
    for rank in range(0, nproc):
        print(split_data[rank])
        print(np.mean(split_data[rank]))
    
    plt.figure()
    plt.hist(assigned_rank)
    plt.show()
    # comm = MPI.COMM_WORLD

