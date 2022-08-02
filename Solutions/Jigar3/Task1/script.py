import requests, json
from bs4 import BeautifulSoup

print("Enter Job Description")
jobDes = raw_input()

print("Enter the Location")
location = raw_input()

obj = requests.get(
    f"https://jobs.github.com/positions.json?description={jobDes}&location={location}"
)


if jsonObj := json.loads(obj.content):
    for j, i in enumerate(jsonObj, start=1):
        print(f"Job {str(j)}" + " ==>\n")
        print("Title: " + i['title'] + "\n")
        print("Location: " + i['location'] + "\n")
        print("Type: " + i["type"] + "\n")
        soup1 = BeautifulSoup(i['description'], "lxml")
        print(f"Description: {soup1.get_text()}" + "\n")
        soup2 = BeautifulSoup(i['how_to_apply'], "lxml")
        print(f"How to Apply: {soup2.get_text()}" + "\n")
        print("Company: " + i["company"] + "\n")
        print("Company Website: " + i["company_url"] + "\n")
        print("---------------------------------------------------------------------")
else:
    print("No Jobs Found")
