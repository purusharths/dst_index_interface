import matplotlib.pyplot as plt
from datetime import datetime
class Plotting(object):
	"""docstring for Plotting"""
	def __init__(self, **kwargs):
		self.year = kwargs.get('year')
		self.month = kwargs.get('month', '')
		self.day = kwargs.get('day', '')

	def get_formatted_date(self, **kwargs):
		year = kwargs.get('year')
		month = kwargs.get('month')
		day = kwargs.get('day', '')
		if day:
			dt_obj = datetime.strptime("{}/{}/{}".format(year, month, day), "%Y/%M/%d")
			return dt_obj.strftime("%B %d, %Y (%A)")
		else:
			dt_obj = datetime.strptime("{}/{}".format(year, month), "%Y/%M")
			return dt_obj.strftime("%B - %Y")

	def normal_plot(self, value, day=True):
		plt.style.use('seaborn')
		plt.plot(value,'o-')
		plt.ylabel("Values")
		if not day:
			plt.xticks(range(0,len(value)))
			plt.xlabel("Days")
			title = self.get_formatted_date(year=self.year, month=self.month)
			plt.title(title)
			plt.show()
		else:
			plt.xticks(range(0,24))
			plt.xlabel("Hours throughout the day")
			title = self.get_formatted_date(year=self.year, month=self.month, day=self.day)
			plt.title(title)
			plt.show()
