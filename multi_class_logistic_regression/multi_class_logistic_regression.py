from numpy import *
import numpy as np
import math
import matplotlib.pyplot as plt
import time

def sigmoid_function(z):
	return 1/(1+np.exp(-z))

def cost_function(data,theta,labels):
	sum=0
	predicted_value = []

	n = len(data)
	for i in range(n):
		x = data[i,:5]
		if data[i,-1] == labels:
			y = 1
		else:
			y=0

		z = sigmoid_function(np.dot(np.transpose(theta), x))
		predicted_value.append(z)

		sum+= (y * math.log(z)) + ((1 - y) * (math.log(1-z)))

	return predicted_value,(-sum)/n

def gradient_descent(data,theta,predicted_value,l_rate,labels):
	a = 0
	b = 0
	c = 0
	d = 0
	e = 0

	n = len(data)
	for i in range(n):
		x = data[i,:5]
		if data[i,-1] == labels:
			y = 1
		else:
			y=0

		diff = predicted_value[i] - y
		a+= x[0] * diff
		b+= x[1] * diff
		c+= x[2] * diff
		d+= x[3] * diff
		e+= x[4] * diff

	a/= n
	b/= n
	c/= n
	d/= n
	e/= n

	theta[0] -= l_rate * a
	theta[1] -= l_rate * b
	theta[2] -= l_rate * c
	theta[3] -= l_rate * d
	theta[4] -= l_rate * d

	return theta

def logistic_regression():

	data=genfromtxt("iris_dataset.csv",delimiter=",")

	'''
	for i in range(len(data)):
		if i<50:
			plt.scatter(data[i,1], data[i,2], label= "0", color= "green",marker= "*", s=30) 
		if i>=50 and i<100:
			plt.scatter(data[i,1], data[i,2], label= "1", color= "blue",marker= "*", s=30)
		else:
			plt.scatter(data[i,1], data[i,2], label= "1", color= "yellow",marker= "*", s=30)

	#plt.show()
	'''
	l_rate = 0.1

	result = []
	test = [1, float(input()), float(input()), float(input()), float(input())]

	for labels in range(3):
		theta=[0, 0, 0, 0, 0]
		loss=[]
		steps=[]

		predicted_value, error = cost_function(data,theta,labels)
		print('Loss for the initial values ',theta,' is ',error)

		for i in range(1000):
			theta = gradient_descent(data,theta,predicted_value,l_rate,labels)

			if i%10 ==0:
				predicted_value, error = cost_function(data,theta,labels)
				loss.append(error)
				steps.append(i)			

		plt.scatter(steps, loss, label= labels,marker= "*", s=30) 
		
		#plt.show()
		print(len(steps),'   ',len(loss))
		
		predicted_value, error = cost_function(data,theta,labels)
		print("Finally,\nLoss for ",theta," is ",error)
	
		result.append(sigmoid_function(np.dot(np.transpose(theta), test)))
		print('predicted output:\n ', result[labels])

	#plt.scatter(test[1],test[2], color= "red", s=30)
	#plt.show()

if __name__== '__main__':
	logistic_regression()

#C:\Users\pvasanth\Desktop\DREAM_PROJECT\hobby\multi_class_logistic_regression
