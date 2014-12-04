from bs4 import BeautifulSoup 
import requests

url = 'http://www.fairmountcemeterypresqueisle.com/map.html'

fairmont_scrape = requests.get(url)

if fairmont_scrape.status_code != 200:
	print("error loading page")

fairmount_html = fairmont_scrape.text

soup = BeautifulSoup(fairmount_html)

data = soup.find_all("option")

for person_data in data:
	print(person_data.text)
	
#now I just need to format this better	
	
	

