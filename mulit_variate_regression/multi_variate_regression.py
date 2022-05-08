from numpy import *
import numpy
import matplotlib.pyplot as plt

def cost_function(data,a,b,c):
	
	n = len(data)
	sum=0

	for i in range(n):
		x_1=data[i,1]
		x_2=data[i,2]
		y=data[i,0] / 100

		sum += ((a*x_1 + b*x_2 + c) - y)**2

	return sum/(2*n)

def gradient_descent(data,a,b,c,l_rate):
	
	new_a = 0
	new_b = 0 
	new_c = 0
	n = len(data)

	for i in range(n):
		x_1=data[i,1]
		x_2=data[i,2]
		y=data[i,0] / 100

		new_a+= (((a*x_1 + b*x_2 + c) - y) * x_1)
		new_b+= (((a*x_1 + b*x_2 + c) - y) * x_2)
		new_c+= ((a*x_1 + b*x_2 + c) - y)

	new_a /= n
	new_b /= n
	new_c /= n

	#print(new_m ,' ',new_c)

	a -= (l_rate * new_a)
	b -= (l_rate * new_b)
	c -= (l_rate * new_c)

	return a,b,c


def linear_regression():

	data=genfromtxt("electricity_charge.csv",delimiter=",")

	a = 0
	b = 0
	c = 0
	l_rate = 0.01

	#for visulization
	loss = []
	coefficient_a = []
	coefficient_b = []
	y_intercept_c = []
	
	x_1 = []
	x_2 = []
	y = []

	for i in range(len(data)):
		x_1.append(data[i,1])
		x_2.append(data[i,2])
		y.append(data[i,0] / 100)

	#plt.show()
	
	print("Cost function for (a)",a," , (b) ",b," and (c)",c," is ",cost_function(data,a,b,c))

	for i in range(1000):
		a, b, c = gradient_descent(data,a,b,c,l_rate)

		if i%10 == 0:
			#print(a,'   ',c)

			loss.append(cost_function(data,a,b,c))
			coefficient_a.append(a)
			coefficient_b.append(b)
			y_intercept_c.append(c)


	print("Finally,\nCost function for (a)",a," , (b) ",b," and (c)",c," is ",cost_function(data,a,b,c))

	electrical_output = float(input())
	labour_cost = float(input())
	print('predicted output:\n ', ((a*electrical_output)+(b*labour_cost)+c)*100)

	xx, yy = numpy.meshgrid(range(5), range(10))

	# calculate corresponding z
	z1 = (a*xx + b*yy + c)

	ax = plt.figure(figsize = (10, 7)).gca(projection='3d')
	ax.plot_surface(xx,yy,z1, color='yellow')
	#ax = fig.add_subplot(111, projection='3d')

	ax.scatter(x_1, x_2, y, marker='X')
	ax.set_xlabel('x')
	ax.set_ylabel('y')
	ax.set_zlabel('z')
	ax.set_zlim(-40, 40)
	ax.set_xlim(0, 5)
	ax.set_ylim(0, 10)

	plt.show()

	'''
	fig = plt.figure(figsize = (10, 7))
	ax = fig.add_subplot(111, projection='3d')

	
	ax.scatter(slope_m, y_intercept_c, loss, marker='o')
	ax.set_xlabel('x')
	ax.set_ylabel('y')
	ax.set_zlabel('z')
	ax.set_zlim(0, 50)
	ax.set_xlim(-5, 5)
	ax.set_ylim(-5, 5)
	plt.show()
	'''

if __name__ == '__main__':
	linear_regression()


#C:\Users\pvasanth\Desktop\DREAM_PROJECT\hobby\mulit_variate_regression