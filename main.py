import argparse
import os
import sys
from generation import generation_main as gm

def main(input_file, output_folder, n_sample, tempo, midis):
    # Example functionality
    print(f"Input file path: {input_file}")
    print(f"Output folder path: {output_folder}")
    print(f"Sample number: {n_sample}")
    print(f"Tempo: {tempo}")
    # Your main code logic goes here
    # check if output folder exists
    if not os.path.exists(output_folder):
        create_folder_prompt_selection = input('WARNING: output folder does not exist. Create it? y/n: ')
        if create_folder_prompt_selection == 'y' or create_folder_prompt_selection == 'Y':
            os.makedirs(output_folder, exist_ok=True)
        else:
            sys.exit('Exiting program, no output folder available.')
    create_midis = midis==1
    for sample in range(n_sample):
        gm.generate_sample(input_file, output_folder, n_sample, sample, tempo, create_midis)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process input arguments for batch script.")
    parser.add_argument("input_file", type=str, help="Path to the input JSON file")
    parser.add_argument("output_folder", type=str, help="Path to the output folder")
    parser.add_argument("n_sample", type=int, help="Number of samples to generate")
    parser.add_argument("tempo", type=int, default=120, help="Tempo with default 120")
    parser.add_argument("midis", type=bool, default=0, help="Create midi files with default 0")

    args = parser.parse_args()

    main(args.input_file, args.output_folder, args.n_sample, args.tempo, args.midis)
