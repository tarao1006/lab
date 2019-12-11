#!/bin/sh
#$ -S /bin/sh
#$ -cwd
#$ -N job
#$ -o std.out -e std.err
#$ -q uni1.q
#$ -v LD_LIBRARY_PATH=/opt/hdf5/1.10.5/lib:/opt/fftw/3.3.8/lib
#$ -pe openmp 4
#$ -v KMP_AFFINITY=verbose,compact,1
#$ -v MKL_NUM_THREADS=4
#$ -v OMP_NUM_THREADS=4
#$ -v MKL_DOMAIN_NUM_THREADS="MKL_ALL=1, MKL_FFT=4"
#$ -v MKL_DYNAMIC=FALSE
#$ -v OMP_DYNAMIC=FALSE
#$ -v OMP_SCHEDULE="static"
# run

~/bin/kapsel -Iinput.udf -Ooutput.udf -Ddefine.udf -Rrestart.udf