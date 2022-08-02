import requests, json
from bs4 import BeautifulSoup

print("Enter Job Description")
jd = raw_input()

print("Enter the Location")
loc = raw_input()
link = (
    f"https://jobs.github.com/positions.json?description={jd}&location={loc}"
)

jobobj = requests.get(link)

if object1 := json.loads(jobobj.text):
    for j, i in enumerate(object1, start=1):
        print(f"Job {str(j)}" + " ==>\n")
        print("Title: " + i['title'] + "\n")
        print("Date added: " + i['created_at'] + "\n")
        print("Location: " + i['location'] + "\n")
        print("Type: " + i["type"] + "\n")
        s1 = BeautifulSoup(i['description'], "lxml")
        print(f"Description: {soup1.getText()}" + "\n")
        print("Company: " + i["company"] + "\n")
        print("Company Website: " + i["company_url"] + "\n")
else:
    print("No Jobs Found")
