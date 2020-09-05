#!/usr/bin/env python
import pandas as pd
import ssl

print('Fetching json Data...')
try:
    ssl._create_default_https_context = ssl._create_unverified_context
    url = 'https://raw.githubusercontent.com/localytics/data-viz-challenge/master/data.json'
    df = pd.read_json(url, orient='split')
except:
    print('Error reading data...')

try:
    df.to_csv('/Users/sarjodas/Downloads/data_output_Step2.csv', index=False)
    print('Data output of Step 2 successfully exported...')
except:
    print('Error writing failed (Please Set export path)...')


print('Computation for Step 3...')
df1 = pd.DataFrame.from_records(df.location.values.tolist()).stack().reset_index()  #unpacking location data
df1.columns = ['index', 'location', 'city']
df2 = df1[df1['location'] == 'state']
df2.reset_index(level=0, inplace=True)
df['date'] = df['client_time'].dt.normalize() # Datetime to date conversion
df['city'] = df2['city']
df['amount']=df['amount'].fillna(0)
df_data = df[(df['city'] == 'CA') & (df['gender'] == 'F')] # Data Frame with Filters

grouped = df_data.groupby(['age', 'device', 'date']) #groupby
total_events = grouped.amount.agg(['size', 'sum']) #aggregation
total_events.reset_index(inplace=True)
#print(total_events)

try:
    total_events.to_csv('/Users/sarjodas/Downloads/total_events_Step3.csv', index=False)
    print('Data output file total_events successfully exported...')
except:
    print('Error writing failed (Please Set export path)...')


