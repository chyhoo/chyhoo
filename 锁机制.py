import threading

VALUE = 0
gLock = threading.Lock()

def add_value():
	# 修改全局变量要声明
	global VALUE
	gLock.acquire()
	for x in range(1000000):
		VALUE +=1
	gLock.release()
	print('VALUE: %d'%VALUE)

def main():
	for x in range(2):
		t = threading.Thread(target=add_value)
		t.start()

if __name__ == '__main__':
	main()