import time

ts = str(time.time())
file = open("saved_time", "w")
file.write(ts)
