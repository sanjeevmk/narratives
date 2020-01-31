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
dirs = ["../child_mortality","../employment","../ghi","../mumbai_locals","../tb","../terrorism"]

peopleAffected = []

for d in dirs:
    csvFiles = list(filter(lambda x:x.endswith(".csv") and 'data' in x,os.listdir(d)))
    csvFiles = [os.path.join(d,fileName) for fileName in csvFiles]
    totalAffected = 0
    for f in csvFiles:
        fData = pd.read_csv(f)
        affectedColumn = fData.iloc[-1,1]
        totalAffected += affectedColumn
    peopleAffected.append([d.split('/')[-1],totalAffected])

print(peopleAffected)

