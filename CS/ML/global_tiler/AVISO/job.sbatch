#!/bin/bash

#SBATCH --job-name=tiler
#SBATCH --mem-per-cpu=30000
#SBATCH --time=00:59:00
#SBATCH --partition=sched_mit_darwin
##SBATCH --partition=newnodes

module load matlab/2013a
matlab -nodisplay -r "gen_sst($1)"

