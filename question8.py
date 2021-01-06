""" Program to generate random logs and write it into a file until it reaches 2 MB. Then opening a new file and continuing  """
from datetime import datetime
import random
import os

default_file = open("defaultDataFile.txt", "r")
count = 1
content_list = list()
for line in default_file:
    pid = random.randint(1000, 9999)
    log_content = line
    # getting the current date and time
    now = datetime.now()
    # converting into string format for ease of appending
    date_time = now.strftime("%d/%m/%Y %H:%M:%S")
    complete_line = date_time + " " + str(pid) + " " + log_content
    content_list.append(complete_line)

while True:
    # Naming the log files as sample_logfile 1, sample_logfile2 and so on...
    writable_log_file_name = "sample_logfile" + str(count) + ".txt"
    log_file = open(writable_log_file_name, "a")
    size = os.stat(writable_log_file_name).st_size
    # if the size is less than 2MB write content else change the name
    if size <= 2000000:
        i = 0
        log_file.write(content_list[i % 5])
        i = i + 1
    else:
        count = count + 1
