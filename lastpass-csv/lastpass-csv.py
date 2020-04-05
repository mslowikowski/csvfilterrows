#!/usr/bin/python3
import argparse

def main():
    parser = argparse.ArgumentParser(description='parse a lastpass csv export and transform it as desired')
    parser.add_argument('--input', help="lastpass csv file to be parsed", required=True)
    parser.add_argument('--output', help="file to save the transformed data", required=True)

    # get the args
    args = parser.parse_args()

if __name__ == "__main__":
    main()