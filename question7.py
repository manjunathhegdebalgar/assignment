""" Program to read the content of log file and write it into a new file with current date time suffix"""
from datetime import datetime

log_file_name = "log_example.log"
new_file = open("new_log_file.log", "w")
list_of_contents = list()
with open(log_file_name, "r") as f:
    for line in f:
        # getting the current date and time
        now = datetime.now()
        # converting into string format for ease of appending
        suffix = now.strftime("%d/%m/%Y %H:%M:%S")
        new_line = suffix + " " + line
        # storing the content in the list with suffix
        list_of_contents.append(new_line)
for i in list_of_contents:
    # writing the contents to file
    new_file.write(i)
