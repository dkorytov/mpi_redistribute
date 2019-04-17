#!/usr/bin/env python2.7

from __future__ import print_function, division

from mpi4py import MPI
import numpy as np
import matplotlib.pyplot as plt

from mpi_redistribute import *

if __name__ == "__main__":
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()
    nproc = 10
    data = np.random.rand(10000*rank)
    id_field = data
    # assigned_rank = assign_id_to_rank(data, nproc)
    # split_data = split_data_by_assigned_rank(assigned_rank, assigned_rank, nproc)
    rank_data = redistribute_data_by_id(data, id_field, comm)
    print(rank, "-> ", len(rank_data))
    # for rank in range(0, nproc):
    #     print(split_data[rank])
    #     print(np.mean(split_data[rank]))
    
    # plt.figure()
    # plt.hist(assigned_rank)
    # plt.show()
    # comm = MPI.COMM_WORLD

