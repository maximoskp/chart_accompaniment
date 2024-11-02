# chart_accompaniment
Includes the submission to MIREX Symbolic Music Generation challenge code.

The python script needs to have the ability to generate folders for temporary files.

1. Setup the environment

Python version: Python 3.11.5

``` bash
conda create -n "chart_acc_gen" python=3.11.5
```

and activate the new environment

``` bash
conda activate chart_acc_gen
```

2. Install requiremements

``` bash
pip install -r requirements.txt
```

3. Make main bash script executable

``` bash
chmod +x batch_acc_gen.sh
```

4. Run bash script with arguments

``` bash
./batch_acc_gen.sh "path_to_input_file.json" "path_to_output_folder" n_sample tempo create_midi_files
```

`tempo` and `create_midi_files` are optional with default values 120 and 0 (false) respectively. If `create_midi_files` is 1 (true), then a `midis` folder will be created within `path_to_output_folder` that includes midi renderings of all output jsons.

Example run:

``` bash
./batch_acc_gen.sh "test_inputs/solar.json" "test_outputs" 5 120 1
```

The first time it runs, it needs to download some models from huggingface (https://huggingface.co/maximoskp/midi_chart_piano_accompaniment/tree/main) so please be patient...

5. Cross your fingers. If it finally runs, prepare your ears for a few seconds of misery!