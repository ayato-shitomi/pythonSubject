import	sys

args = sys.argv

str = args[1]
n = int(args[2])

m = 0
while (m < n):
	print(str * n)
	m = m + 1