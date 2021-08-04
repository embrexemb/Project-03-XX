# -*- coding: UTF-8 -*-
import os
import csv
import string

city_list=[]
markers=[]

def clean_markers(m_city_list):
    h_locations=[]
    cleaned=[]
    for x in m_city_list:
        clen=(len(x) -1)
        print(f'original string is {clen}')
        cleaned.append(x[7:clen])
    print(cleaned)
    for x in cleaned:
        #new=x.split(",",1)
        h_locations.append(x.split(",",1))
    return(h_locations)


with open('hotel.csv', newline='') as csvfile:
    reader=csv.DictReader(csvfile)
    for row in reader:
       #print(row['City'])
        city_list.append(row['City'])

print(f'city is {city_list}')

markers=clean_markers(city_list)
print(f'cleaned markers are {markers}')





