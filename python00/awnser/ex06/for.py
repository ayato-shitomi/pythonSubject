import	sys

argv = sys.argv

for i in argv:
	if (i == __file__):
		pass
	else:
		print(i)