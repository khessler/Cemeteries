from bs4 import BeautifulSoup 
import requests

#I'd like to be able to go through the list to then run through a second request, to automate scraping of multiple cemeteries--but not sure how to do that.  Can I do this without an API?
# url for list of maine cemeteries in BillionGraves: http://billiongraves.com/pages/search/#country=United+States&state=Maine&county=0&search_text=&action=search_cemetery&start=0&limit=100&is_admin=0
#payload = {'country': 'United States', 'state': 'Maine', 'county': 0}
#r = requests.get("http://billiongraves.com/pages/search", params = payload)

#scraping a single cemetery here

url = 'http://billiongraves.com/pages/cemeteries/Pine-Grove-Cemetery/47294'

cem_page = requests.get(url)

if cem_page.status_code != 200:
	print("error loading page")

cem_html = cem_page.text

soup = BeautifulSoup(cem_html)

#here is the cemetery name 
cem_name = soup.find("h2", attrs = {"id": "cem_name"})
print(cem_name.text) #will eventually write this to file...

#also the town/state
cem_address = soup.find("span", attrs = {"id": "cemLoc"})
print(cem_address.text)

#and latitude/longitude
cem_coordinates = soup.find("div", attrs = {"id": "cemeteryCoordinates"})
print(cem_coordinates.text)

#all_graves = soup.find_all("li", attrs = {"class": "ng-scope"})

#for a_name in all_graves:
	#gah can I do some sort of find all, or extraction based on the element type? I need to keep the names and dates together (matched), 
	#print(a_grave.text), got nothing (no error though)
	#a_name = soup.find("a", attrs = {"class": "ng-binding"})
	#print(a_name.text)
	
#for date_range in all_graves:

	#date_range = soup.find("div", attrs = {"class": "recordYears ng-binding"})
	#print(date_range.text)
	
#maybe instead of printing, a function here to combine name & date and THEN print?

#def combine_info(a_name, date_range)
	#print(a_name, date_range)
	
#what format would be best for a data dump? csv?