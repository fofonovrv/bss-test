import time

from datetime import datetime
while True:
	with open("/var/log/test3.log", "a") as f:
		message = f'test3.service: я всё еще работаю  {str(datetime.now())} \n'
		f.write(message)
		f.close()
	time.sleep(10)