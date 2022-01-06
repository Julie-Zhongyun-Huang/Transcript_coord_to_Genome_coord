#!/usr/bin/env python3

import argparse
import logging
import os
import sys
import pandas as pd
import re

def make_arg_parser():
    parser = argparse.ArgumentParser(description='python3 trans_to_genome.py ' \
                                 '--input_file_1_path path to input file_1.txt' \
                                 '--input_file_2_path path to input file_2.txt' \
                                 '--output_file_path path to output file')
    parser.add_argument("--input_file_1_path", required=True)
    parser.add_argument("--input_file_2_path", required=True)
    parser.add_argument("--output_file_path", required=True)
    return parser

def convert_cigar_string_to_list(cigar):
    '''
    Use regex to convert the CIGAR string into a list of (value, type)
    eg. [(8, M), (7, D), (6, M)]
    '''
    cigar_list = re.findall(r'(\d+)(\w)', cigar)
    return cigar_list    

def transcript_coord_to_genome_coord(hang, cigar, tr_coord):
    '''
    Input the hang number (str), cigar (string) and coordiate of the nt in the transcript
    ouput the genome coordinate of the alignment
    '''
    genome_output = int(hang) - 1 # accomodate for 0-based index
    tr_remain = int(tr_coord) + 1 # accomodate for 0-based index
    
    cigar_list = convert_cigar_string_to_list(cigar)
    for value, cigar_type in cigar_list:
        if int(tr_remain) == 0:
            break
        if cigar_type == "M":
            genome_output += min(int(value), tr_remain)
            tr_remain -= min(tr_remain, int(value))
        elif cigar_type == "D":
            genome_output += int(value)
        elif cigar_type == "I":
            tr_remain -= min(tr_remain, int(value))
    return str(genome_output)

def main(argv):
    # set up the parser
    parser = make_arg_parser()
    args = parser.parse_args()
    if not args.input_file_1_path:
        logging.error("---- invalid input_file_1")
    elif not os.path.isfile(args.input_file_1_path):
        logging.error("---- empty input file 1")
    else:
        input_file_1_path = args.input_file_1_path 
    if not args.input_file_2_path:
        logging.error("---- invalid input_file_2")
    elif not os.path.isfile(args.input_file_2_path): 
        logging.error("---- empty input file 2")
    else:
        input_file_2_path = args.input_file_2_path
    if not args.output_file_path:
        logging.error("--- invalid output file name")
    else:
        output_file_path = args.output_file_path
    # set up the log file
    output_dir = "/".join(output_file_path.split("/")[0:-1])
    log_file_name = '{}/transcript_to_genomics_coord.log'.format(output_dir)
    logging.basicConfig(filename=log_file_name, level = logging.INFO, format = '%(asctime)s:%(name)s:%(levelname)s:%(message)s')
    logger = logging.getLogger('trans_to_genome')
    if os.path.exists(log_file_name):
        os.remove(log_file_name)
    # set up output file
    output_file = open(output_file_path, "w")
    # read input_file_1 as a pandas df
    input_file_1 = pd.read_csv(input_file_1_path, sep="\t", header = None, index_col=0)
    # read input_file_2 line by line, calculate genomic coord, and write to output_file line by line 
    input_file_2 = open(input_file_2_path, "r")
    for line in input_file_2:
        trans_ID, tr_coord = line.strip().split("\t")[0], line.strip().split("\t")[1]
        tr_chr, hang, cigar = input_file_1.loc[trans_ID, 1], input_file_1.loc[trans_ID, 2], input_file_1.loc[trans_ID, 3]
        genome_coord = transcript_coord_to_genome_coord(hang, cigar, tr_coord)
        L = [trans_ID, tr_coord, tr_chr, genome_coord]
        logger.info('\t'.join(L))
        output_file.write('\t'.join(L))
        output_file.write('\n')
    input_file_2.close()
    output_file.close()
    logger.info("--- the conversion is complete")

if __name__ == "__main__":
        main(sys.argv)
