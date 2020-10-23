import os
import re
import csv

# give path to csv file containing the survey emails
with open('email2.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)[0]

# give path to csv file containing email addresses from a dump
with open('dump.csv', newline='') as f:
    reader = csv.reader(f)
    dump = list(reader)[0]

# change this path to wherever you are storing the pastes
folder = 'PASTEBIN API/scraps'

reader = ''
for entry in os.scandir(folder):
    with open(entry.path, 'r') as f:
        reader += f.read()

# add to existing dump list
dump += re.findall(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', reader)

intersection = list(filter(lambda x: x in dump, data))
# should print out any email addresses from our testing list if found in any of the pastes or dumps
print(intersection)
