import sys
args = sys.argv

if 0 == int(args[1]):
	print("数字は0です")
elif 0 < int(args[1]):
	print("数字は正です")
else:
	print("数字は負です")