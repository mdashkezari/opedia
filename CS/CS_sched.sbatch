#!/bin/bash

#SBATCH --job-name=Lagran
#SBATCH --mem-per-cpu=30000
#SBATCH --time=12:00:00
#SBATCH --partition=sched_mit_darwin

module load matlab/2013a
matlab -nodisplay < CS_job.m



##day_start=$1
##day_end=$2

#for (( day=$1; day<=$2; day++  ))
#do 
#	for i in {1..2}
#	do
#		for j in {1..4}
#		do
##			sbatch -p sched_system_all --mem-per-cpu 10000 -n 1 edML.py $day $i $j
#			sbatch -p sched_mit_darwin --mem-per-cpu 10000 -n 1 edML.py $day $i $j
##			sbatch -p newnodes --mem-per-cpu 20000 -n 1 edML.py $day $i $j
#			echo $day,$i,$j
#		done
#	done
#done
