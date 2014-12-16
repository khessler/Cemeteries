import requests, json

r = requests.get('http://billiongraves.com/pages/search/scripts/cemetery_finder.php?country=United+States&state=Maine&county=0&search_text=&action=search_cemetery&start=0&limit=100&is_admin=0')

print(r.status_code)

#print(r.text)

#run it into a python dictonary

data = json.loads(r.text)

print(data)
 
