# Convert Transcript Coordinate to Genome Coordinate

## Dependencies
This version needs Python(3.6.0)

## Usage
python3 trans_to_genome.py \
        --input_file_1_path /Users/huangz36/Documents/invitae_DC/example/input_file_1.txt \
        --input_file_2_path /Users/huangz36/Documents/invitae_DC/example/input_file_2.txt \
        --output_file_path /Users/huangz36/Documents/invitae_DC/example/output_file.txt

## Input parameters
| Parameter       | Description                          | Notes |
| --------------- | ------------------------------------ | ----- |
| input_file_1_path | The path to input file 1 | A four column (tab-separated) file containing the transcripts. |
| input_file_2_path | The path to input file 2 | A two column (tab-separated) file indicating a set of queries. |
| output_file_path  | The path to the output file | A four column tab separated file with one row for each of the input queries  |

## Example
Please see the example folder

## Contact
This module was developed by Julie Huang: zhongyunbell@gmail.com
Last update of the README file: Jan 7th, 2022
