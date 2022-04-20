import time

text = "Hello World!"
for i in text:
    print (i, end = '',flush = True)
    time.sleep(.1)
time.sleep(1)
