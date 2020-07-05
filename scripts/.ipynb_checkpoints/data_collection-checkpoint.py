import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from time import sleep


url = 'https://www.truecar.com/used-cars-for-sale/listings/location-jersey-city-nj/?searchRadius=25'

r = requests.get(url, headers={
                        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
                        'referer':'https://www.google.com/'})
soup = BeautifulSoup(r.text, features="html.parser")

last_page = int(soup.find('li', attrs={'data-test':'mobilePageRange'}).text[-2:])

car_name = []
price = []
mill = []
loca = []
his = []

for page in range(last_page):    
    
    url = 'https://www.truecar.com/used-cars-for-sale/listings/location-jersey-city-nj/?page=' + str(page) +'&searchRadius=25'

    
    r = requests.get(url, headers={
                        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
                        'referer':'https://www.google.com/'})

    
    soup = BeautifulSoup(r.text, features="html.parser")

    listings = soup.find_all('div',attrs={'data-qa':'Listings'})


    for i in range(len(listings)):
        try:
            car_name.append(listings[i].find('a', attrs={'data-test':'usedListing'}).find('div',attrs={'data-test':'cardContent'}) \
                    .find('div', attrs={'data-test':'vehicleCardYearMakeModel'}).text)
        except:
            car_name.append('nothing')
            
        try:
            price.append(listings[i].find('a', attrs={'data-test':'usedListing'}).find('div',attrs={'data-test':'cardContent'}) \
                    .find('div', attrs={'data-test':'vehicleListingPriceAmount'}).text.strip())
        except:
            price.append(0)
        
        try:
            mill.append(listings[i].find('a', attrs={'data-test':'usedListing'}).find('div',attrs={'data-test':'cardContent'}) \
                    .find('div', attrs={'data-test':'vehicleMileage'}).text)

                    
        except:
            mill.append(0)
        
        try:
            loca.append(listings[i].find('a', attrs={'data-test':'usedListing'}).find('div',attrs={'data-test':'cardContent'}) \
                    .find('div', attrs={'data-test':'vehicleCardLocation'}).text)
        except:
            loca.append('nothing')

        try:
            his.append(listings[i].find('a', attrs={'data-test':'usedListing'}).find('div',attrs={'data-test':'cardContent'}) \
                    .find('div', attrs={'data-test':'vehicleCardCondition'}).text)
        except:
            his.append('nothing')
    
    sleep(10)
    

col_nams = ['car_name', 'price', 'millage', 'location', 'history']
col_data = [car_name, price, mill, loca, his]

df = pd.DataFrame(data=col_data, index=col_nams).T

df.to_csv('../data/raw_data.csv', index=False)


