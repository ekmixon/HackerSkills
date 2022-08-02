from bs4 import BeautifulSoup
import requests

document = requests.get("https://scirate.com/")
soup = BeautifulSoup(document.content, "html.parser")

titles = soup.select(".title a")
links = soup.find_all("a", attrs={'title': "Download PDF"})
for i, title in enumerate(titles):
    print(f"Title: {title.text}")
    if(i<len(links)):
        print("Link: " + links[i]['href'])
    print("---------------------------------------------------------------------")
