import csv
import pandas as pd
import re


df = pd.read_excel(io='Int_Air_Carrier.xlsx', sheet_name="Sheet1")
#creating a header
header = df.iloc[0]
#replacing the dataframe with a new one that does not have the header
df = df[1:]
df.rename(columns=header)
# # # How could I have done this faster??? # # #
#header_1 = ['Observation','Outdoor','Social','Conservative','Anxiety','JOB','JID','Age']
#df.rename(columns=header_1)
#df.set_index('Observation')
print(df.head(4))

#for key,value in df['Observation'].iteritems():
    #print(key,value)
#df["Observation"] = pd.to_string(df['Observation'])
#print(df.head(3))
#print(df.info())
#df['Observation'] = df['Observation'].



#### OTHER WAYS OF READING THE FILE #####

# # # Looping through # # # 
#with open('Int_Air_Carrier.csv') as csvfile:
    #readCSV = csv.reader(csvfile, delimiter=',')
    #column_1 = []
    #column_2 = []
    #print(readCSV)
    

    #for row in readCSV:
        #column_1 += row[0]
        #row[1] = column_2
        #print(column_1)

# # # Into an object # # # 
#f = open('Int_Air_Carrier.csv','r')
#csvreader = csv.reader(f)
#print(csvreader)

# # # Observations into an ordered dictionary # # #
#with open('Int_Air_Carrier.csv', newline='') as csvfile:
    #reader = csv.DictReader(csvfile)
    #for dct in map(dict, reader):
        #print(dct)
    #for row in reader:
        #print(row)