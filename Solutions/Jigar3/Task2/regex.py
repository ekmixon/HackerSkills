import re

date = raw_input("Enter the date in DD-MM-YYYY format\n")
regex = re.compile(r'(\d\d)-(\d\d)-(\d\d\d\d)')
rGroups = regex.search(date)

print("Converted the date in MM/DD/YYYY format->")
print(rGroups[2] + "/" + rGroups[1] + "/" + rGroups[3])
