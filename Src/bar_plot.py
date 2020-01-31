import pandas as pd
import numpy as np
import csv
import seaborn as sns
import sys
import os
import matplotlib.pyplot as plt
import json
from matplotlib import rcParams
import matplotlib.style as style

config = sys.argv[1]
args = json.loads(open(config,'r').read())
sns.set()
style.use("seaborn-white")
rcParams['figure.figsize'] = 22,22
rcParams['axes.labelsize'] = 40 
rcParams['axes.titlesize'] = 48 
rcParams['xtick.labelsize'] = 32 
rcParams['ytick.labelsize'] = 32 
rcParams['text.color'] = "darkslategrey"
rcParams['xtick.color'] = "darkslategrey"
rcParams['ytick.color'] = "darkslategrey"
rcParams['axes.labelcolor'] = "darkslategrey"
DisplayTextName = "TopText"

dataFile = args['Data']
Xname = args['X']
Yname = args['Y']
#palette = args['Color']
#palette = "YlOrRd"
palette = "Reds"
outputFile = args['Output']
title = args['Title']
df = pd.read_csv(dataFile)
df.columns = [Xname,Yname,DisplayTextName]
pal = sns.color_palette(palette, len(df))
rank = df[Yname].argsort().argsort()
g = sns.barplot(x=Xname,y=Yname,data=df,palette=np.array(pal)[rank])

for index,row in df.iterrows():
    g.text(row.name,row[Yname]+0.01*row[Yname],str(row[DisplayTextName]),ha='center',color='darkslategrey',fontsize=36)
plt.box(on=None)
plt.title(title)
plt.ticklabel_format(style='plain', axis='y')
plt.savefig(outputFile,bbox_inches='tight',pad_inches=0)
#plt.show()