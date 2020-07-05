import numpy as np
import pandas as pd

df =  pd.read_csv('../data/raw_data.csv')

#Separate year, make and model

df['car_name'] = df['car_name'].str.replace('Sponsored','')
df.loc[:,'year'] = df['car_name'].apply(lambda x: x.split()[0])
df.loc[:,'make'] = df['car_name'].apply(lambda x: x.split()[1])
df.loc[:,'model'] = df['car_name'].apply(lambda x: ' '.join(x.split()[2:]))
df.drop('car_name',axis=1,inplace=True)

#Convert price and millage into numbers, removing literal characters
df['price'] = pd.to_numeric(df['price'].str.replace('$','').str.replace(',',''))
df['millage'] = pd.to_numeric(df['millage'].str.replace(' miles','')
                              .str.replace(',',''))

#Convert location into only city and state

df.loc[:,'city'] = df['location'].apply(lambda x: x.split('-')[1]).apply(lambda x: x.split(',')[0])
df.loc[:, 'state'] = df['location'].apply(lambda x: x.split('-')[1]).apply(lambda x: x.split(',')[1])
#df.drop('location', axis=1, inplace=True)
# Removing the blank space at the start of the city name
df['city'] = df['city'].apply(lambda x : x.strip())
# Joining City and State,
df.loc[:, 'location'] = df['city'] + ', ' + df['state']

#Split the history column into 3 categories: accidents and owners are numerical.
df.loc[:, 'accidents'] = pd.to_numeric(df['history']
                                       .apply(lambda x:x.split(',')[0])
                                       .apply(lambda x: x.split(' ')[0])
                                       .str.replace('No','0'))
df.loc[:, 'owners'] = pd.to_numeric(df['history']
                                    .apply(lambda x:x.split(',')[1])
                                    .apply(lambda x:x.split()[0]),
                                                errors='coerce',
                                                downcast='integer')
df.loc[:,'use'] = df['history'].apply(lambda x:x.split(',')[-1]).apply(lambda x:x.split()[0])
df.drop('history', axis=1, inplace=True)


#Only consider the cars with a price tag.
df = df.loc[df['price']>0]

# Combining make and model into vehicle name
df.loc[:,'name'] = df['make'] + ' ' + df['model']

#df.drop(['make','model','city','state'], axis=1,inplace=True)



df.to_csv('../data/clean_data.csv', index=False)