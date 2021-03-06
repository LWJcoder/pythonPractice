#coding :utf-8

class Date(object):
	def __init__(self, day=0, month=0, year=0):
		self.day = day
		self.month = month
		self.year = year

	def __str__(self):
		return "{0}-{1}-{2}", format(self.year,self.month, self.day)

	@classmethod
	def from_string(cls, date_as_str):
		year, month , day = map(int, date_as_str.split('-'))
		date1 = cls(day, month, year)
		return date1

	@staticmethod
	def is_date_valid(date_as_str):

		year, month , day = map(int, date_as_str.split('-'))
		return year <= 3999 and month <= 12 and day<= 31


	@staticmethod
	def milleniun(month, day):
		return Date(month, day, 2000)

class DateTime(Date):
	"""docstring for DateTime"""
	def __str__(self):
		return "{0}-{1}-{2} - 00:00:00 pm", format(self.year, self.month, self.day )
		


if __name__ == '__main__':
	s = '2012-09-12'
	if Date.is_date_valid(s):
		date1 = Date.from_string('2012-09-12')
		print date1
		date2 = DateTime.from_string('2013-02-12')
		print date2
		