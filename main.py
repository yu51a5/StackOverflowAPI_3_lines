import requests

url = f"https://api.stackexchange.com/2.3/questions?tagged=stackexchange-api&site=stackoverflow"
result = requests.get(url)
print(result.text)
