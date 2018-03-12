import sys
from calendar import monthrange
import json

import get_data
import plotting

def display_error(arg=""):
	if arg:
		print(arg)
	print("Command line argument not present or invalid. Try again.")
	print("Use python main.py <year> <month> <day (optional)> ")
	print("Eg: python main.py 1997 12 ")
	print("Further flags include: --table-html, --table-cli, --plot-days, --sublplot")

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





def cla():
	val = True
	try:
		year = sys.argv[1]; month = sys.argv[2]
	except IndexError:
		display_error();exit()
	try:
		if int(year) > 2013 or int(year) < 1950:
			print("Year beyond the range. Exiting...\n"); display_error(); exit()
		if int(month) < 1 or int(month) > 12:
			print("Invlaid Month. Exiting...\n"); display_error(); exit()
	except ValueError:
		print("Invalid Numerical Value");exit()
	try:
		day = sys.argv[3]
		if int(day)>31 or int(day) < 1:
			print("Invalid Dates. Exiting...\n"); display_error(); exit()
		limit = monthrange(int(year), int(month))[1]
		if int(day) > limit:
			print("Invalid Date for given month and year. Exiting...\n");display_error();exit()
		try:
			if not sys.argv[4]:
				val = get_day(year, month, day)
		except:
			pass
	except IndexError:
		pass
	try:
		if sys.argv[4]:
			plot_points = get_day(year, month, day, rtr=True); val=False
			pl = plotting.Plotting(year=year, month=month, day=day)
			pl.normal_plot(plot_points)
			return "plotted"
	except IndexError:
		pass
	if val:
		get_data.main(year, month)

if __name__ == '__main__':
	cla()
