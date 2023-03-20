from mpi4py import MPI

def main():
    passes = 5
    id = ""
    rank = MPI.COMM_WORLD.Get_rank()
    comm = MPI.COMM_WORLD
    if rank == 0:
        id = "Player 0"
        next = 1
    else:
        id = "Player 1"
        next = 0
    if rank == 0:
        print(f"Number of parallel players is {comm.Get_size()}")
        comm.send("Player 0 has initiated",dest=1,tag=0)
    
    while passes > 0:
        message = comm.recv(source=next, tag=0)
        print(f"{id} received the message :- {message}")
        comm.send(f"{id}s pass number {5-passes + 1}",dest=next,tag=0)
        passes-=1
    print(f"Passes over for {id}")

if __name__ == "__main__":
    main()