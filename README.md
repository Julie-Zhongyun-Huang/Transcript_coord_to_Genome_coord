# Convert Transcript Coordinate to Genome Coordinate

## Dependencies
This version needs Python(3.6.0)

## Usage
python3 trans_to_genome.py \
        --input_file_1_path /Users/huangz36/Documents/invitae_DC/example/input_file_1.txt \
        --input_file_2_path /Users/huangz36/Documents/invitae_DC/example/input_file_2.txt \
        --output_file_path /Users/huangz36/Documents/invitae_DC/example/output_file.txt

## Assumptions
Assumption 1: I assumed "Input file 2", column 2 to only contain valid transcript coordinates. Exception happens when the coordinate is larger than the total length of the cigar string (sum of M and I numbers of the string). When the coordinate is invalid, for the specific query row, I output "-1" to the column 4 space, indicating the invalid coordinate. Please see example/input_file_2.2.txt row 3, and corresponding example/output_file_2.txt row 3. 

Assumption 2: I assumed "input file 1" to contain limited number of transcripts, while "input file 2" the query list is long. I have thus read in the "input file 1" as a pandas dataframe for faster look up using the transcript ID, and to obtain chromosome, start coordinate and CIGAR information more quickly. However, the memory efficiency is not ideal if the "input file 1" is too large. If the "input file 1" is a large file, while the "input file 2" has fewer queries, consider to read in "input file 1" line by line instead of pd.dataframe, use "startwith" to screen for the line that contains the trasncript ID in the query, and perform the same functions. Depending on the sizes of "input file 1" and "input file 2", I may consider to sort the files first to facilitate faster searching of "chromosome", "start_coord" and "CIGAR" information for each query.  

## Key strength and weakness
Strength: only reads in the "input file 1" once, and performs quick look up for transcript information. High time efficiency when performing batch query with long "input file 2". Logging is used to report error messages when the input file is not valid. 

Weakness: uses memory to save the "input file 1" as a dataframe. Also not time efficient when "input file 1" contains a large number of transcripts, while the query only limited to few transcripts. 

## Input parameters
| Parameter       | Description                          | Notes |
| --------------- | ------------------------------------ | ----- |
| input_file_1_path | The path to input file 1 | A four column (tab-separated) file containing the transcripts. |
| input_file_2_path | The path to input file 2 | A two column (tab-separated) file indicating a set of queries. |
| output_file_path  | The path to the output file | A four column tab separated file with one row for each of the input queries  |

## 

## Example
Please see the example folder
Created examples for the following cases
1. Both input_file_1 and input_file_2 valid
2. Input_file_1 is empty
3. Input_file_1 contains wrong number of columns
4. Input_file_2 is empty
5. Input_file_2 contains wrong numbver of columns
6. Input_file_2 has the transcript coord in the query larger than the CIGAR string allows

## Contact
This module was developed by Julie Huang: zhongyunbell@gmail.com
Last update of the README file: Jan 7th, 2022
