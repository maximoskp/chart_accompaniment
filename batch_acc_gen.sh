#!/bin/bash

# Check if at least three arguments are provided
if [ "$#" -lt 3 ]; then
  echo "Usage: $0 /path/to/input.json /path/to/output_folder n_sample tempo midis"
  exit 1
fi

# Assign input arguments to variables
input_file="$1"
output_folder="$2"
n_sample="$3"
tempo="${4:-120}"  # Tempo argument with default value if not provided
midis="${5:0}"  # Create midis argument with default value if not provided

echo input_file: "$input_file"
echo output_folder: "$output_folder"
echo n_sample: "$n_sample"
echo tempo: "$tempo"
echo midis: "$midis"

# Call the Python script with the provided arguments
python main.py "$input_file" "$output_folder" "$n_sample" "$tempo" "$midis"
