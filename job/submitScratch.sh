#!/bin/bash
 

module add engaging/python/2.7.11
module add engaging/unixODBC/2.3.4 
cd ~/opedia

sbatch -p sched_mit_darwin --mem-per-cpu 64000 -n 1 oscratch.py $1 $2 $3 $4 $5

#for (( day=$4; day<=$5; day++  ))
#do
#	sbatch -p sched_mit_darwin --mem-per-cpu 10000 -n 1 oscratch.py $1 $2 $3 $day $day
#done
