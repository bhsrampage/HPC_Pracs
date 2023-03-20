from mpi4py import MPI
import random

random.seed(random.random())

def slave_work(rank):
    steps = random.randint(1,10)
    for i in range(steps):
        print(f"Slave Rank {rank} is working for {i+1} step")

rank = MPI.COMM_WORLD.Get_rank()
comm = MPI.COMM_WORLD
slave_work(rank)
comm.Barrier()
data = ""
data = comm.bcast(data,root=0)
print(f"Slave Rank {rank} receives {data}")