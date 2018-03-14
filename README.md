# Geomagnetic Equatorial Dst Index Interface (CLI and Web Application)

## Introduction
The Dst index is an index of magnetic activity derived from a network of near-equatorial geomagnetic observatories that measures the intensity of the globally symmetrical equatorial electrojet (the "ring current") <br/>
 
## About the interface
There are two interfaces. Command line interface (on `master` branch) and Webapp interface (on `webapp` branch)
There is also a `.sqlite` database which keeps a cashed copy of all the indices that have aldready been searched for to preserve bandwidth.

## Usage
For either of the interface, switch to the branch and do <br/>
`pip install -r requirements.txt`
### 1. Command Line Interface
*To get readings for a month* <br/>
`python main.py --year <year> --month <month>` <br/>
or  <br/>
`python main.py -y <year> -m <month>`<br/>
*To get result for a specific day* <br/>
`python main.py --year <year> --month <month> --day <day>` <br/>
or <br/>
`python main.py -y <year> -m <month> -d <day>`<br/>
#### Plot Options (CLI)
The flag `--plot-days` and `--plot-month` are used for getting matplotlib graphs for the given day / month (average value for each day of the month). <br/>
Example: <br/>
`python main.py --year 1969 --month  12 --day 12 --plot-days`

### 2. Web Application
This web application is based on Flask Microframework. Make sure that flask is installed and run: <br/>
`python app.py` <br/>
The live version is up on heroku can be accessed <a href="https://dstindex.herokuapp.com"> here </a>.
