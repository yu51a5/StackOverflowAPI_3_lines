import requests
import datetime

for which, sort_order in (('very first', 'asc'), ('most recent', 'desc')):
  url = f"https://api.stackexchange.com/2.3/questions?page=1&pagesize=1&order={sort_order}&sort=creation&site=stackoverflow"
  result = requests.get(url).json().get("items")[0]
  dt = datetime.datetime.fromtimestamp(result['creation_date']).strftime('%Y %b %d at %H:%M:%S')
  print(f"The {which} Stack Overflow question was created on {dt}.\nIts title is `{result['title']}`.\n") 
