#!/usr/bin/env python
import pdb
import csv
from c45 import C45
#pdb.set_trace()
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder #install necessary package
from os.path import basename,splitext

filename="pgwebwln.csv" 
fname=splitext(basename(filename))
fileprefix=fname[0]
fname=fileprefix+'.data'
dataset=pd.read_csv(filename)
reader=csv.reader(open(filename),delimiter=',')
counter=0
x=dataset.iloc[:,:].values
i=0

for row in reader:
	if counter==1:
		firstrow=row
		break
	else:
		counter+=1			
i=0
encodeindex=[]
for col in firstrow:
	if firstrow.index(col)<len(firstrow)-1 and not col.isdigit():
				encodeindex.append(i)
	i+=1

le=LabelEncoder()
for i in encodeindex:
	x[:,i]=le.fit_transform(x[:,i])

np.savetxt(fname,x,fmt='%s',delimiter=',')

c1 = C45(fileprefix+".data", fileprefix+".names")
c1.fetchData()
c1.preprocessData()
c1.generateTree()
c1.printTree()
