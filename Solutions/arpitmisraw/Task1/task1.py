import requests
from bs4 import BeautifulSoup

description = input("Enter Description: ")
location = input("Enter Location: ")
loc = list(location.split(" "))
location = "".join(f"+{loc_element}" for loc_element in loc)
url = f"https://jobs.github.com/positions?description={description}&location={location}"

resp = requests.get(url)

html = resp.text
soup = BeautifulSoup(html)


title = soup.select('.title h4 a')

for job_title in title:
    print("\n\n" + job_title.getText() + "\n")
    url_job = "https://jobs.github.com" + job_title.get('href')
    job_req = requests.get(url_job)
    job_html = job_req.text
    job_soup = BeautifulSoup(job_html)
    info = job_soup.select('.column.main')
    link = job_soup.select('.highlighted a')
    for job_info in info:
        print(job_info.getText())
    print("\nApply here: " + link[0].get('href'))
    print("\n\n")

