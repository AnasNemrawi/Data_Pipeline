import requests
import pandas as pd
from datetime import datetime, timedelta, timezone
import matplotlib.pyplot as plt
import schedule
import time

print('-----------the code takes some time to run and get all the data please wait ---------')

api_key = "a3f87a3a568b4db5a94e3cba05fe1772"

def fetch_data(api_key, date):
    url = f"https://openexchangerates.org/api/historical/{date}.json?app_id={api_key}&symbols=USD,SAR"
    response = requests.get(url)
    data = response.json()["rates"]
    data['Date'] = date # adding a row of dates 
    return data

"""
In the API documentation, it is possible to use a time.series end point, however, you need a paid account to use it. 
In order to get data on my end, I have used for loop to hit the route 90 times to retrieve all data one by one,
    the following comment is how I would ideally write the code if I had access to the paid service.
"""
"""
def fetch_data(api_key, startDate, endDate):
    url = f"https://openexchangerates.org/api/time-series.json?app_id={api_key}&start={startDate}&end={endDate}&symbols=BTC,EUR,HKD&prettyprint=1"

    response = requests.get(url)
    data = response.json()["rates"]
    return data
"""

def save_data(df, filename):
    try:
        existing_data = pd.read_csv(filename)
    # delete the existing data
        existing_data.iloc[0:0].to_csv(filename, index=False)
    except FileNotFoundError:
        pass
    df.to_csv(filename,date_format='%m-%d', index=True)
    print("Data saved to comparison_data.csv")


def compare_currency(api_key):
    current_date = datetime.now(timezone.utc)
    # the following for loop is also used to retrive data 90 times .you would not need to use it if you have access to the paid subscription.
    date_range = [(current_date - timedelta(days=i)).strftime("%Y-%m-%d") for i in range(90)]

    all_data = []

    for date in date_range:
        data = fetch_data(api_key, date)
        all_data.append(data)

    df_all_data = pd.DataFrame(all_data)
    df_all_data['Date'] = pd.to_datetime(df_all_data['Date'])
    df_all_data.set_index('Date', inplace=True)

    # Save the SAR data to CSV
    save_data(df_all_data[['SAR']], "comparison_data.csv")
    
    # display the data using matplotlib
    plt.plot(df_all_data.index, df_all_data['SAR'], label='SAR')
    plt.xlabel('Date')
    plt.ylabel('Exchange Rate')
    plt.title('USD to SAR Exchange Rate Over 3 months')

    plt.xticks(df_all_data.index[::9])
    
    plt.show()
    return df_all_data

Comparison = compare_currency(api_key)

# schedule to run the code every 24 h

schedule.every(24).hours.do(compare_currency, api_key)

while True:
    schedule.run_pending()
    time.sleep(1)
