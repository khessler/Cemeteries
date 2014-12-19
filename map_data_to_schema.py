import json

with open("people_data_n100.json") as people_data:
	r = json.loads(people_data.read())

all_new_records = []
	
for record in r:
	if "lat" in record:
		latitude = record["lat"]
	else:
		latitude = None
	if "lon" in record:
		longitude = record["lon"]
	else:
		longitude = None		
	new_record = {
    "@id": record["url"],
    "name": record["fullname"],
    "lifespan": {
    	"birth": record["birth_year"],
    	"death": record["death_year"]
    },
    "cemetery_name": record["cemetery_name"],  
    "location":{
    	"city": record["cemetery_city"],
    	"state": record["cemetery_state"],
		"latitude": latitude,
		"longitude": longitude
    	}   
}

	all_new_records.append(new_record)
	
with open('12.10.2014records_n100.json', 'w') as outfile:
	json.dump(all_new_records, outfile, indent=4)
	