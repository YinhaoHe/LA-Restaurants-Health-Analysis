import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns
# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will fac_per the files in the input directory
import os
# print(os.fac_perdir("../la-restaurant-market-health-data"))
import json

inspections = pd.read_csv('../la-restaurant-market-health-data/restaurant-and-market-health-inspections.csv', parse_dates=['activity_date'])
inspections_raw = inspections.copy()
inspections.set_index('serial_number', inplace=True)

violations = pd.read_csv('../la-restaurant-market-health-data/restaurant-and-market-health-violations.csv', parse_dates=['activity_date'])
violations_raw = violations.copy()

inspections = inspections[inspections.service_description == 'ROUTINE INSPECTION']
inspections = inspections[inspections.program_status == 'ACTIVE']

cols = ['activity_date', 'employee_id', 'facility_id', 'record_id', 'pe_description',
       'score', 'grade']

inspections = inspections[cols]

# print(inspections.head(3))
##########################################
daily_inspections = pd.DataFrame(inspections.groupby(['activity_date'])['facility_id'].nunique())
daily_inspections.reset_index(inplace=True)
# print(daily_inspections.head(3))
# print(type(daily_inspections))
# for date in daily_inspections:
# 	print(date.activity_date, date.facility_id)

# Number of facilities visited perday
fac_per = []
for row in daily_inspections.itertuples(index=True, name='Pandas'):
    # print(pd.to_datetime(getattr(row, "activity_date"), unit='s'), getattr(row, "facility_id"))
    # print(getattr(row, "activity_date").strftime('%Y-%m-%d'), getattr(row, "facility_id"))
    fac_per.append([getattr(row, "activity_date").strftime('%Y-%m-%d'), getattr(row, "facility_id")])
print (fac_per)

with open('JSON1.json','w') as f:
    json.dump(fac_per,f)
##########################################