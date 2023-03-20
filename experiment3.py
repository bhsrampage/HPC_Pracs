from mpi4py import MPI
import numpy as np
n = 10

comm = MPI.COMM_WORLD
size = MPI.COMM_WORLD.Get_size()
rank = MPI.COMM_WORLD.Get_rank()
# print(rank,size)
prnt_ctr = 0
ctr = 0
a = np.zeros(100)
master = 0
elements_per_process = int(n/size)

if rank == master:
    if size > 1:
        for i in range(1,size-1):
            #print(f"sent {i}")
            index = i*elements_per_process
            comm.send(elements_per_process,i,0)
            comm.send(index,i,1)
            
        index = (size-1)*elements_per_process
        elements_left = n - index
        comm.send(elements_per_process,(size-1),0)
        comm.send(index,(size-1),1)
        #print(f"Sent to last process {(size-1)}")
    cube = 0
    for i in range(elements_per_process):
        cube = pow(i,3)
        print(f"{prnt_ctr}^3 = {cube}")
        prnt_ctr+=1
    for i in range(1,size): 
        ctr = comm.recv(source=i,tag=2)
        a = comm.recv(source=i,tag=3)
        for j in range(ctr):
            print(f"{prnt_ctr}^3 = {a[j]}")
            prnt_ctr+=1
else:
    elements_received = comm.recv(source=master,tag=0)
    #print(elements_received)
    index = comm.recv(source=master,tag=1)
    partial_sum = 0
    for i in range(elements_received):
        a[i] = pow(index+i,3)
    #print(a)
    comm.send(elements_received,master,2)
    comm.send(a,master,3)








