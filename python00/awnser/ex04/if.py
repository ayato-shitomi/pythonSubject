import	sys

num = int(sys.argv[1])

if (num == 0):
	print("数字は0です")
elif (num < 0):
	print("数字は負です")
elif (0 < num):
	print("数字は正です")
