#!/usr/bin/python3
"""an inheritated class mylist"""

class Mylist(list):
	"""implement sorted in built in clas lists"""

	def print_sorted(self):
		"""print a list in a sorted ascending order"""
		print(sorted(self))
