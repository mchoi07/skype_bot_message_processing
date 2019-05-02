f = open("/home/evan/skype_bot_message_processing/test_output.txt", "w")
import test_count

count = test_count.count
f.write("I updated this " + str(count) + " times")
count += 1

c = open("/home/evan/skype_bot_message_processing/test_count.py", "w")
c.write("count = " + str(count))

f.close()
c.close()
