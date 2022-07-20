from ast import arg
from asyncio import subprocess
import	subprocess as sb
import	os

def	run(path, args, out):
	komsg = ">> KO <<"
	if (os.path.exists(path)):
		cmd = "python3 " + path + " " + args
		result = sb.run(cmd, shell=True, check=True, stdout=sb.PIPE, universal_newlines=True)
		n = 0
		if (len(result.stdout.splitlines()) != len(out)):
			return (komsg)
		for line in result.stdout.splitlines():
			if (line != out[n]):
				return (komsg)
			n = n + 1
		return ("   OK")
	else:
		return ("file does not exist.")


# ex00
path = "./ex00/print.py"
args = ""
out = ["HELLO"]
print(path, args, "\t\t", run(path, args, out))

# ex01
path = "./ex01/print_some.py"
args = ""
out = ["hello <class 'str'>", "HELLO <class 'str'>", "123 <class 'str'>", "123 <class 'int'>"]
print(path, args, "\t\t", run(path, args, out))

# ex02
path = "./ex02/type.py"
args = ""
out = ["[1, 2, 3] <class 'list'>", "1 <class 'int'>", "2 <class 'int'>", "3 <class 'int'>"]
print(path, args, "\t\t\t", run(path, args, out))

# ex03
path = "./ex03/arg.py"
args = "hello"
out = ["hello"]
print(path, args, "\t\t", run(path, args, out))

# ex04
path = "./ex04/if.py"

args = "0"
out = ["数字は0です"]
print(path, args, "\t\t\t", run(path, args, out))
args = "100"
out = ["数字は正です"]
print(path, args, "\t\t", run(path, args, out))
args = "-100"
out = ["数字は負です"]
print(path, args, "\t\t", run(path, args, out))

# ex05
path = "./ex05/while.py"
args = ""
out = ["Hello 0", "Hello 1", "Hello 2"]
print(path, args, "\t\t", run(path, args, out))

# ex06
path = "./ex06/for.py"

args = "a1 a2 a3"
out = ["a1", "a2", "a3"]
print(path, args, "\t\t", run(path, args, out))
args = "1 2 3"
out = ["1", "2", "3"]
print(path, args, "\t\t", run(path, args, out))

# ex07
path = "./ex07/put_sqare.py"
args = '"##" 10'
out = ["####################","####################","####################","####################","####################","####################","####################","####################","####################","####################"]
print(path, args, "\t", run(path, args, out))
args = '"#" 0'
out = []
print(path, args, "\t", run(path, args, out))
