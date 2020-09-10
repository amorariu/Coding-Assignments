# Implementation of CauchyList class
import random

# class definition
class CauchyList:
# initialization of variables
	def __init__(self, p):
		self.content = []
		self.p = p
# initialization list randomly
	def generate_random(self, n):
		for i in range(n):
			self.content.append(random.randint(0,self.p-1))
		print(self.content)
# length function
	def length(self):
		return len(self.content)
# get function
	def get(self, i):
		if i < self.length():
			return self.content[i]
		else:
			return 0
# add operator overloading
	def __add__(self, obj1):
		try:
			if self.p != obj1.p:
				raise ValueError()
		    newSize = max(self.length(), obj1.length())
		    obj = CauchyList(newSize)
		    for i in range(newSize):
			    obj.content.append((self.get(i) + obj1.get(i))%self.p);
		    print(obj.content)
		    return obj
		except ValueError:
		    print("Oops! Value of P must be same for both Cauchy List!")

	def __sub__(self, obj1):
		try:
			if self.p != obj1.p:
				raise ValueError()
			newSize = max(self.length(), obj1.length())
			obj = CauchyList(newSize)
			for i in range(newSize):
				obj.content.append((self.get(i) - obj1.get(i))%self.p);
			print(obj.content)
		    return obj
		except ValueError:
			print("Oops! Value of P must be same for both Cauchy List!")

	def __mul__(self, obj1):
		try:
			if self.p != obj1.p:
				raise ValueError()
			newSize = self.length() + obj1.length() -1
			obj = CauchyList(newSize)
			minSize = min(self.length(), obj1.length())
			temp = 0
			for i in range(newSize):
				for j in range(minSize):
					temp = temp + self.get(j) * obj1.get(j-minSize);
				obj.content.append(temp%self.p)
			print(obj.content)
			return obj
		except ValueError:
			print("Oops! Value of P must be same for both Cauchy List!")


def __str__(self):
return("p: "+str(self.p)+"\nlength: "+str(self.length())+"\ncontent: "+str(self.content))


# Testing
cl = CauchyList(8)
cl.generate_random(10)

cl2 = CauchyList(10)
cl2.generate_random(10)

cl3 = cl + cl2
cl4 = cl - cl2
cl5 = cl * cl2

print(cl3)