import sys

def a1():
	print('a1 executed')

def a2():
	print('a2 executed')

def _exec(func=a1):
	print(func, type(func),type(func+'()'), type('a1()'))
	exec(func+'()')
	print('*'*10)
	eval(func+'()')

if __name__ == "__main__":
	if len(sys.argv) > 1:
		_exec(sys.argv[1])
	print("{}".format(str(sys.argv)))#sys.argv[1]))