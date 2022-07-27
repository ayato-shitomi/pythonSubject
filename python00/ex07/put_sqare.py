from ast import arg
import sys
args = sys.argv
i = 0
while i < int(args[2]):
	print(args[1] * int(args[2]))
	i += 1