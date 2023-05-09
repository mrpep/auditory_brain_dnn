#!/bin/bash
#SBATCH --job-name=inhouse-20230509
#SBATCH --time=00:10:00
#SBACTH --ntasks=1
#SBATCH --output="out/inhouse-20230509-%j.out"
#SBATCH --mem=1G
#SBATCH -p evlab

source /mindhive/mcdermott/u/gretatu/anaconda/etc/profile.d/conda.sh
conda activate auditory_brain_dnn

set -x

cd /mindhive/mcdermott/u/gretatu/auditory_brain_dnn/aud_dnn/
python AUD_main.py --source_model "${1}" --source_layer "${2}" --randnetw "${3}" --target "${4}"