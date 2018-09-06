// /* -*- Mode: C; c-basic-offset:4 ; indent-tabs-mode:nil ; -*- */
// /*
//  *  (C) 2001 by Argonne National Laboratory.
//  *      See COPYRIGHT in top-level directory.
//  */

#include <stdio.h>
#include "mpi.h"


  /* Local functions */



int main(int argc, char *argv[])
{
	int rank, size;


	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	MPI_Comm_size(MPI_COMM_WORLD, &size);

	printf("Hello world from process %d of %d\n", rank, size);

	if (rank == 0)
	{
		// master();
		MPI_Status s;
		int Sstate = 1;
		int Rstate;

		int p;
		for (p = size - 1; p >= 0; p--) {

			//fflush(stdout);
			printf("master : order P%d to start reading\n", p);
			MPI_Send(&Sstate, sizeof(int), MPI_INT, p, 20, MPI_COMM_WORLD);

			MPI_Recv(&Rstate, sizeof(int), MPI_INT, p, 21, MPI_COMM_WORLD, &s);
			//fflush(stdout);
			printf("master : P%d finished reading\n", p);
		}
	}
	else
	{
		int state;
		MPI_Status s;
		printf("begin recieve\n");
		MPI_Recv(&state, sizeof(int), MPI_INT, 0, 20, MPI_COMM_WORLD, &s);

		//read here
		sleep(1000);
		printf("end recv and begin send\n");

		//send to master : finish reading
		state = 2;
		MPI_Send(&state, sizeof(int), MPI_INT, 0, 21, MPI_COMM_WORLD);
		printf("end send\n");

		//processing
		sleep(3000);
		fflush(stdout);
		printf("worker %d ended processing\n", rank);


		//slave();
	}


	///printf("[P_%d] process %d said: \"%s\"]\n", rank, recvfrom, inbuf);

	MPI_Finalize();
	return 0;
}
