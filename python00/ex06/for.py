import sys
args = sys.argv
i = 0
for a in args:
	if i == 0:
		i += 1
		continue
	print(f"{args[i]}")
	i += 1