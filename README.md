# CSV Filter Rows

This python script filters rows from a CSV file that contain values with lengths exceeding a specified maximum.

## Basics

    usage: csvfilterrows.py [-h] [-m MAXIMUM] -i INPUT -o OUTPUT

    Parse a lastpass csv export and transform it as desired.

    optional arguments:
    -h, --help            show this help message and exit
    -m MAXIMUM, --maximum MAXIMUM
                            The maximum length of an entry (default = 10000)
    -i INPUT, --input INPUT
                            The LastPass csv file to be parsed
    -o OUTPUT, --output OUTPUT
                            The output file to save the transformed data

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [Deployment](#Deployment) for notes on how to use the script.

### Prerequisites

What software you will need to work on this script

1. [Visual Studio Code](https://code.visualstudio.com/Download) - Any IDE will do
2. [Docker](https://docs.docker.com/get-docker/)
3. [Python](https://www.python.org/downloads) [Optional] - This script was developed using Python 3.8, other versions may work.  Development and running can (and probably should) be done entirely in a container.

### Building

From the commandline you can do the following

1. Build the docker image

    ```Shell
    docker build -t csvfilterrows .
    ```

2. Run the container

    ```Shell
    docker run -it --rm  csvfilterrows
    ```

    This example runs the script which returns the help information.

    ```Shell
    docker run -it --rm -v ./data:/data csvfilterrows -i /data/in.csv -o /data/out.csv -m 1000
    ```

    This example demo creates a volume to map a ```./data``` directory on the local host to the ```/data``` directory in the container.  You should change the first directory to match the path of the directory with the file(s) you want to manipulate.
