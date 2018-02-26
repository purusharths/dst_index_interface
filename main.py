import sys

import get_data


def display_error():
	print("Command line argument not present. Try again.")
	print("Use python main.py <year> <month> <day (optional)> ")
	print("Eg: python main.py 1997 12 ")
	print("Further flags include: --table-html, --table-cli, --plot, --sublplot")

def cla():
	try:
		year = sys.argv[1]; month = sys.argv[2]
	except IndexError:
		display_error();exit()
	try:
		if int(year) > 2013 or int(year) < 1950:
			print("Year beyond the range. Exiting...");exit()
		if int(month) < 1 or int(month) > 12:
			print("Invlaid Month. Exiting...");exit()
	except ValueError:
		print("Invalid Numerical Value");exit()
	get_data.main(year, month)

if __name__ == '__main__':
	cla()