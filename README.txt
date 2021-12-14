Several parallel GeMM implementations with OpenMP and OpenBLAS.

1. OpenMP_v1/v2:
    1.0 brew install clang-omp
    1.1 g++ gemm_old.cpp -fopenmp -O3
    1.2 python loop.py
2. OpenBLAS:
    2.0 cd ~ ; git clone https://github.com/xianyi/OpenBLAS.git ; cd OpenBLAS ; make install PREFIX=~/blas USE_OPENMP=1 target=x86_64
    2.1 export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/username/blas/lib
    2.2 g++ gemm.cpp -fopenmp -O3 -I ~/blas/include -L ~/blas/lib -lopenblas -lpthread
    2.3 python loop.py

Thanks for:
    https://samma.hse.ru
    https://hpc.hse.ru/instructions/ssh
    http://www.ccfit.nsu.ru/~kireev/
    https://fossies.org/linux/OpenBLAS/USAGE.md
    
