#!/bin/sh
#$ -S /bin/sh
#$ -cwd
#$ -pe openmp 2
#$ -m be
#$ -v LD_LIBRARY_PATH=/opt/hdf5/1.10.5/lib:/opt/fftw/3.3.8/lib
#$ -v KMP_AFFINITY=verbose,compact,1
#$ -v MKL_NUM_THREADS=2
#$ -v OMP_NUM_THREADS=2
#$ -v MKL_DOMAIN_NUM_THREADS="MKL_ALL=1, MKL_FFT=2"
#$ -v MKL_DYNAMIC=FALSE
#$ -v OMP_DYNAMIC=FALSE
#$ -v OMP_SCHEDULE="static"

python job.py
