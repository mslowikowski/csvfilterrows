#!/usr/bin/python3
import argparse
import os

os.environ['COLUMNS'] = "80"
defaultMaximum = 1000

def main():
    parser = argparse.ArgumentParser(description='Parse a lastpass csv export and transform it as desired.', )
    parser.add_argument('-m', '--maximum', help=f"The maximum length of an entry (default = {defaultMaximum})", required=False, default=defaultMaximum)
    parser.add_argument('-i', '--input', help="The LastPass csv file to be parsed", required=True)
    parser.add_argument('-o', '--output', help="The output file to save the transformed data", required=True)
    # get the args
    args = parser.parse_args()

if __name__ == "__main__":
    main()