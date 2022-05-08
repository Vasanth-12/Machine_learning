from numpy import *
import numpy as np
import math
import matplotlib.pyplot as plt
import time

def sigmoid_function(z):
	return 1/(1+np.exp(-z))

def cost_function(data,theta):
	sum=0
	predicted_value = []

	#n = len(data)
	n=100
	for i in range(n):
		x = data[i,:5]
		y = data[i,-1]

		z = sigmoid_function(np.dot(np.transpose(theta), x))
		predicted_value.append(z)

		sum+= (y * math.log(z)) + ((1 - y) * (math.log(1-z)))

	return predicted_value,(-sum)/n

def gradient_descent(data,theta,predicted_value,l_rate):
	a = 0
	b = 0
	c = 0
	d = 0
	e = 0

	n = len(data)
	n=100
	for i in range(n):
		x = data[i,:5]
		y = data[i,-1]

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

	theta=[0, 0, 0, 0, 0]
	l_rate = 0.1

	loss=[]
	steps=[]

	predicted_value, error = cost_function(data,theta)
	print('Loss for the initial values ',theta,' is ',error)

	for i in range(1000):
		theta = gradient_descent(data,theta,predicted_value,l_rate)

		if i%10 ==0:
			predicted_value, error = cost_function(data,theta)
			loss.append(error)
			steps.append(i)
			'''
			x=[0,1,2,3,4,5,6,7]
			y=[]
			for i in range(8): 
				y.append(theta[0] + theta[1]*i + theta[2]*i)
			'''
			#plt.plot(x,y)
			

	plt.scatter(steps, loss, label= "stars", color= "green",marker= "*", s=30) 
	'''
	for i in range(100):
		if i<50:
			plt.scatter(data[i,1], data[i,2], label= "0", color= "green",marker= "*", s=30) 
		if i>=50:
			plt.scatter(data[i,1], data[i,2], label= "1", color= "blue",marker= "o", s=30)
	
	x=[0,1,2,3,4,5,6,7]
	y=[]
	for i in range(8): 
		y.append(theta[0] + theta[1]*i + theta[2]*i*(1/4))

	plt.plot(x,y)
	#plt.show()
	print(len(steps),'   ',len(loss))
	'''
	predicted_value, error = cost_function(data,theta)
	print("Finally,\nLoss for ",theta," is ",error)

	#sepal_length = float(input())
	#sepal_width = float(input())
	#petal_length = float(input())
	#petal_width = float(input())
	#print('predicted output:\n ', sigmoid_function(theta[0]*sepal_length + theta[1]*sepal_width + theta[2]*petal_length + theta[3]*petal_width))
	
	test = [1, float(input()), float(input()), float(input()), float(input())]
	print('predicted output:\n ', sigmoid_function(np.dot(np.transpose(theta), test)))

	#for i in range(100):
	#	print(i,'   ',predicted_value[i])

	#plt.scatter(test[1],test[2], color= "red", s=30)
	plt.show()



if __name__== '__main__':
	logistic_regression()

#C:\Users\pvasanth\Desktop\DREAM_PROJECT\hobby\logistic_regression
