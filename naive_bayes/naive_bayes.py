import pandas as pd
import csv

def find_propability(df,key,value,label,label_name):
	n = len(df)

	x = len(df[(df[key]==value) & (df[label_name]==label)])

	likehood = len(df[(df[key]==value) & (df[label_name]==label)]) / len(df[(df[label_name]==label)]) 

	evidance = len(df[(df[key]==value)]) / n

	return likehood/evidance

def naive_bayes():
	import pandas as pd
	df = pd.read_csv('health_check.csv', sep=',')
	#df = pd.read_csv('tennis.csv', sep=',')
	print(df)

	header = df.columns
	label_name = header[-1]
	value = []
	for i in range(len(header)-1):
		value.append(input())

	posterior_propability = 1
	for i in range(len(value)):
		if value[i] != '-1':
			posterior_propability *= find_propability(df,header[i],value[i],'yes',label_name)

	prior_probability = len(df[(df[label_name]=='yes')])/ len(df)

	print('propability of yes', posterior_propability * prior_probability)

	posterior_propability = 1
	for i in range(len(value)):
		if value[i] != '-1':
			posterior_propability *= find_propability(df,header[i],value[i],'no',label_name)

	prior_probability = len(df[(df[label_name]=='no')])/ len(df)
	print('propability of no', posterior_propability * prior_probability)

if __name__ == '__main__':
	naive_bayes()


#C:\Users\pvasanth\Desktop\DREAM_PROJECT\hobby\naive_bayes

#df[(df.C=='foo') & (df.A==2.0)]