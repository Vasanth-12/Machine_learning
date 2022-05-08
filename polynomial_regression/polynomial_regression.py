from numpy import *
import matplotlib.pyplot as plt

def cost_function(data,a,b,c):
	
	n = len(data)
	sum=0

	for i in range(n):
		x=data[i,0]
		y=data[i,-1]

		sum += ((a*x*x + b*x + c) - y)**2

	return sum/(2*n)

def gradient_descent(data,a,b,c,l_rate):
	
	new_a = 0
	new_b = 0 
	new_c = 0
	n = len(data)

	for i in range(n):
		x=data[i,0]
		y=data[i,-1] 

		new_a+= (((a*x*x + b*x + c) - y) * x*x)
		new_b+= (((a*x*x + b*x + c) - y) * x)
		new_c+= ((a*x*x + b*x + c) - y)

	new_a /= n
	new_b /= n
	new_c /= n

	#print(new_m ,' ',new_c)

	a -= (l_rate * new_a)
	b -= (l_rate * new_b)
	c -= (l_rate * new_c)

	return a,b,c


def linear_regression():

	data=genfromtxt("polynomial_data.csv",delimiter=",")

	a = 0
	b = 0
	c = 0
	l_rate = 0.000377

	#for visulization
	loss = []
	coefficient_a = []
	coefficient_b = []
	y_intercept_c = []
	
	'''
	x=[]
	y=[]

	for i in range(len(data)):
		x.append(data[i,0])
		y.append(data[i,-1])

	print(x)
	print(y)

	#plt.scatter(x, y, label= "stars", color= "green",marker= "*", s=30) 
	#plt.show()
	'''
	
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

	x = int(input())
	print('predicted output:\n ', (x*a*x)+(b*x)+c)

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


#C:\Users\pvasanth\Desktop\DREAM_PROJECT\hobby\polynomial_regression