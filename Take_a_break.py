import webbrowser
import time

total_breaks = 5
break_count = 0

print("This program started on " + time.ctime())
print(time.gmtime(0))
while (break_count < total_breaks):
    time.sleep(10)
    webbrowser.open("https://www.google.com/")
    break_count += 1

