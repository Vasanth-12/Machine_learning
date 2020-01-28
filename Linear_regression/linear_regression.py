#adding comment line from GUI
from numpy import *

def compute_error_function(m,c,pt):
	total_error=0
	n=float(len(pt))

	for i in range(0,len(pt)):
		x=pt[i,0]
		y=pt[i,1]
		total_error+=(y-(x*m -c))**2
	return total_error/n

def main_gradient_descent(current_m,current_c,pt,l):
	m_gradient=0
	c_gradient=0
	n=float(len(pt))

	for i in range(0,len(pt)):
		x=pt[i,0]
		y=pt[i,1]

		m_gradient+=(-2/n)*(y-(x*current_m - current_c))*x
		c_gradient+=(-2/n)*(y-(x*current_m - current_c))

	new_m=current_m - l*m_gradient
	new_c=current_c - l*c_gradient
	return [new_m,new_c]

def fun_gradient_descent(m,c,pt,learning_rate,iteration):
	for i in range(iteration):
		m,c=main_gradient_descent(m,c,pt,learning_rate)
	return [m,c]

def learn_linear_regression():

	#importing the data file
	pt=genfromtxt("data1.csv",delimiter=",")

	#declare slope_m,y_intercept_c,learning_rate,iteration
	slope_m=0
	y_intercept_c=0
	learning_rate=0.0001
	iteration=1000

	print("error for initial_value ",slope_m,y_intercept_c,compute_error_function(slope_m,y_intercept_c,pt))

	slope_m,y_intercept_c=fun_gradient_descent(slope_m,y_intercept_c,pt,learning_rate,iteration)
	print("optimal value of m and c and error:  ",slope_m,y_intercept_c,compute_error_function(slope_m,y_intercept_c,pt))

	#print("predict ")
	x=int(input())
	print("predicted value of ",x, " is",(x*slope_m)+y_intercept_c)

if __name__=="__main__":
	learn_linear_regression();
