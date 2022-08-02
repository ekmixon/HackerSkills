import re

date =str(input())
dateregex = re.compile(r'(\d\d)-(\d\d)-(\d\d\d\d)')
verify = dateregex.search(date)
if verify is None:
	print("Date input form not Valid")
else:
	print(verify[2] + "/" + verify[1] + "/" + verify[3])