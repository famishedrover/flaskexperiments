import requests

auth = ('admin','admin')
r = requests.get('http://localhost:5000/secret',auth=auth)

print r.content
