import os

myCmd = 'srun -N 1 --ntasks-per-node=1 --cpus-per-task={} --sockets-per-node=1 ./a.out {} {} {} >> file_result'
for i in [1, 2, 4, 16, 24]:
	for j in [500, 1000, 1500]:
		os.system(myCmd.format(i, j, 10, i))
		os.system("echo "" >> file_result")
