

for (( day=$1; day<=$2; day++  ))
do
	sbatch job.sbatch $day
        echo $day
done
