import requests
from pprint import pprint
from config import api_key
import json
# Get user input for stock Ticker
ticker = "IBM"
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+ticker+'&outputsize=compact&apikey=api_key'
r = requests.get(url)
data = r.json()

#json.dumps converts list of dictionary to json string.
jsonString = json.dumps(data['Time Series (Daily)'])

#opens new file
jsonFile = open("data.json", "w")
jsonFile.write(jsonString)
jsonFile.close()
pprint(data['Time Series (Daily)'])