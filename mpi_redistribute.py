
from mpi4py import MPI
import numpy as np

def assign_id_to_rank(id_field, nproc, hash_function = hash):
    assigned_rank = np.zeros_like(id_field, dtype=int)
    for i in range(0, len(id_field)):
        assigned_rank[i]= hash_function(id_field[i])%nproc
    return assigned_rank

def split_data_by_assigned_rank(data, assigned_rank, nproc):
    result = []
    for rank in range(0, nproc):
        slct = assigned_rank == rank
        result += [data[slct]]
    return result

def redistribute_data_by_assigned_rank(data, assigned_rank, comm):
    nproc = comm.Get_size()
    split_data = split_data_assigned_rank(data, assigned_rank, comm)
    redistrubted_data = np.concatenate(comm.alltoall(split_data))
    return redistrubted_data

def redistribute_data_by_id(data, id_field, comm):
    nproc = comm.Get_size()
    assigned_rank = assign_id_to_rank(id_field, nproc)
    split_data = split_data_by_assigned_rank(data, assigned_rank, nproc)
    redistrubted_data = np.concatenate(comm.alltoall(split_data))
    return redistrubted_data



