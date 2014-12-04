import requests, json

payload = {'action': 'browse', 'cemetery_id': '47294', 'lim': '0', 'num': '25'}
indiv_data = requests.get('http://billiongraves.com/pages/cemetery/scripts/searchCemeteryRecords.php', params=payload)

print(indiv_data.status_code)

#print(indiv_data.text)

people_data = json.loads(indiv_data.text)
 
with open('people_data.json', 'w') as outfile:
  json.dump(people_data, outfile)

