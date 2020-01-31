import pandas as pd
import numpy as np
import csv
import seaborn as sns
import sys
import os
dataFile = sys.argv[1]
output = 'data.csv'

df = pd.read_csv(dataFile,encoding='iso-8859-1',low_memory=False)
df = df[((df['crit1']==1) & (df['crit2']==1) & (df['crit3']==1)) & (df['doubtterr']==0)]
startYear = 2008
endYear = 2018

outputRows = [['year','nkill','nwound']]
for year in range(startYear,endYear+1):
    ydf = df[df['iyear']==year]
    cdf = ydf[ydf['country_txt']=='India']
    nkill = cdf['nkill'].sum()
    nwound = cdf['nwound'].sum()
    outputRows.append([str(year),str(int(nkill)),str(int(nwound))])

csv.writer(open(output,'w'),delimiter=',').writerows(outputRows)