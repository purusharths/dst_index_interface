# Geomagnetic Equatorial Dst Index Interface (CLI and Web Application)

## Introduction
The Dst index is an index of magnetic activity derived from a network of near-equatorial geomagnetic observatories that measures the intensity of the globally symmetrical equatorial electrojet (the "ring current") <br/>
 
## About the interface
There are two interfaces. Command line interface (on `master` branch) and Webapp interface (on `webapp` branch)
There is also a `.sqlite` database which keeps a cashed copy of all the indices that have aldready been searched for to preserve bandwidth.

## Usage
For either of the interface, switch to the branch and do <br/>
`pip install -r requirements.txt`
### Command Line Interface
`python main.py --year <year> --month <month> --day <day>`

### 
