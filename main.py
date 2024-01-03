import requests
import datetime

now = datetime.datetime.now()

for which, sort_order in (('very first', 'asc'), ('most recent', 'desc')):
  url = f"https://api.stackexchange.com/2.3/questions?page=1&pagesize=1&order={sort_order}&sort=creation&site=stackoverflow"
  result = requests.get(url).json().get("items")[0]
  dt = datetime.datetime.fromtimestamp(result['creation_date'])
  delta = now - dt
  delta_sec = delta.seconds + delta.days * 24*60*60
  delta_str = (f'{delta_sec} second{"s" if delta_sec > 1 else ""} ago') if (delta_sec > 0) else 'just now'

  print(f"""The {which} Stack Overflow question was created on {dt.strftime('%d %b %Y at %H:%M:%S')},
                                                      {delta_str},
            Its title is `{result['title']}`.
            Its URL is `{result['link']}`.\n""") 
