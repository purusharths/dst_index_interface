
'''
parser = argparse.ArgumentParser()
parser.add_argument("name")
parser.add_argument("Age")
args = parser.parse_args()

print(args.name)

if args.name == 'magic.name':
        print 'You nailed it!'


import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                            help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                            const=sum, default=max,
                                                help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args)
print(args.accumulate(args.integers))
'''

import argparse
import datetime
from calendar import monthrange
import json

import get_data
import plotting

def get_day(year, month, day, rtr=False):
        response = get_data.get_value_from_database(year, month, day)
        if response:
                print("\n YEAR: {} | MONTH: {} | DAY: {}".format(year, month, day))
                print(response[0][1])
                if rtr:
                        return json.loads(response[0][1])
                else:
                        return 1
        else:
                get_data.main(year,month,display=False)
                get_day(year, month, day)


def cla(year, month, day, plot_day):
    if day!='None':
        limit = monthrange(int(year), int(month))[1]
        if int(day) > limit:
            print("Invalid Date for given month and year. Exiting...\n")
            exit()
        val = get_day(year, month, day)
    elif not day and month and year:
        print(month, year, day)
        get_data.main(year, month)
    
    if plot_day:
        try:
            plot_points = get_day(year, month, day, rtr=True); val=False
            pl = plotting.Plotting(year=year, month=month, day=day)
            pl.normal_plot(plot_points)
            return "plotted"
        except IndexError:
            pass

if __name__ == '__main__':

    def str2bool(v):
        if v.lower() in ('yes', 'true', 't', 'y', '1'):
            return True
        elif v.lower() in ('no', 'false', 'f', 'n', '0'):
            return False
        else:
            raise argparse.ArgumentTypeError('Boolean value expected.')

    parser = argparse.ArgumentParser('My program')
    parser.add_argument('-y', '--year', type=int, choices=range(1957,2014))
    parser.add_argument('-m', '--month', type=int, choices=range(1,13))
    parser.add_argument('-d', '--day', type=int, choices=range(1,32))
    parser.add_argument('--plot-day', type=str2bool, nargs='?', const=True)
    args = vars(parser.parse_args())
    n = lambda x: ('0'+str(x)) if len(str(x)) == 1 else str(x)

    cla(str(args['year']), n(args['month']), n(args['day']), args['plot_day'])

'''
import argparse
import datetime

parser = argparse.ArgumentParser()
parser.add_argument('date', type=lambda s: datetime.datetime.strptime(s,'%Y-%m-%d'))
args = parser.parse_args()  # For testing.  Pass no argument in production
year = args.date.year
if year > 2013 or year < 1957:
    print("Invalid year argument! Year range is between 1957 to 2013. Try Again.")
    exit()
month = args.date.month
date =  args.date.day
'''