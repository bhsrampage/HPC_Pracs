from mpi4py import MPI
import random

random.seed(random.random())

def master_work(rank):
    steps = random.randint(1,10)
    for i in range(steps):
        print(f"Master Rank {rank} is working for {i+1} step")

rank = MPI.COMM_WORLD.Get_rank()
comm = MPI.COMM_WORLD
master_work(rank)
comm.Barrier()
comm.bcast("Mission is a success",root=rank)
