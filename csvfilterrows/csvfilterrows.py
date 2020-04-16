#!/usr/bin/python3
import argparse
import os
import csv

os.environ['COLUMNS'] = "80"
defaultMaximum = 10000

def max_len(str_list):
    maxlen = -1
    for ele in str_list:
        if len(ele) > maxlen: 
            maxlen = len(ele)
    return maxlen

def main():
    parser = argparse.ArgumentParser(description='Parse a lastpass csv export and transform it as desired.', )
    parser.add_argument('-m', '--maximum', help=f"The maximum length of an entry (default = {defaultMaximum})", required=False, default=defaultMaximum, type=int)
    parser.add_argument('-i', '--input', help="The LastPass csv file to be parsed", required=True)
    parser.add_argument('-o', '--output', help="The output file to save the transformed data", required=True)
    # get the args
    args = parser.parse_args()

    lp_file = open(args.input,"r")
    with open(args.input, newline='') as lpfile:
        with open(args.output, 'w') as outfile:
            reader = csv.reader(lpfile)
            writer = csv.writer(outfile)
            for row in reader:
                if max_len(row) < args.maximum:
                    writer.writerow(row)

if __name__ == "__main__":
    main()