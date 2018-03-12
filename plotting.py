import matplotlib.pyplot as plt

class Plotting(object):
	"""docstring for Plotting"""
	def __init__(self, **kwargs):
		self.year = kwargs.get('year')
		self.month = kwargs.get('month', '')
		self.day = kwargs.get('day', '')

	def normal_plot(self, value, day=True):
		if not day:
			pass
		else:
			plt.style.use('ggplot')
			plt.plot(value,'o-')
			plt.xticks(range(0,24))
			plt.xlabel("Hours Through The Day")
			plt.ylabel("Values")
			title = "Dst Index for {}/{}/{}".format(self.year, self.month,self.day)
			plt.title(title)
			plt.show()		
