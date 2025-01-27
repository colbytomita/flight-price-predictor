import serpapi
import pandas as pd
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")

params = {
  "engine": "google_flights",
  "departure_id": "HNL",
  "arrival_id": "ICN",
  "outbound_date": "2025-11-20",
  "return_date": "2025-11-30",
  "currency": "USD",
  "hl": "en",
  "api_key": api_key
}

search = serpapi.search(params)
results = search.as_dict()
price_insights = results["price_insights"]

def convert_price_history_to_utc(price_history):
    updated_history = []
    for entry in price_history:
        timestamp, price = entry
        utc_time = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
        updated_history.append([utc_time, price])
    return updated_history

# Update the price history
price_insights['price_history'] = convert_price_history_to_utc(price_insights['price_history'])
# print(results)

# df = pd.DataFrame(price_insights)

print(price_insights)
