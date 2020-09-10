
# this program implements the cauchy list

import random

class CauchyList: 
    
    def __init__(self, p):
        self.p = p
        self.content = []

    def generate_random(self, n):
        # given the range of n, it selects random numbers and stores
        # it into an array content
        for ii in range(n):
            self.content.append(random.randint(0, self.p-1))
        

    def length(self):
        # returns the value of the number of elements in the list
        return len(self.content)

    def get(self, i):
        # if the is in the range then take the length of the object
            if i < len(self.content):
                return self.content[i]
            else:
                return 0

    def __add__(self, b):
        # allocating the value of p to b 
        if self.p != b.p:
            raise ValueError("p is not the same")
        Size = max(self.length(), b.length())
        item = CauchyList(self.p)
        for i in range(Size):
            item.content.insert(i,(self.get(i) + self.get(i) % self.p))
        return item
    def __sub__(self, b):
        #__sub__ does the same operation as __add__ but
        # the end product is subtracted not added
        if self.p != b.p:
            raise ValueError("p is not the same")
        Size = max(self.length(), b.length())
        item = CauchyList(self.p)
        for i in range(Size):
            item.content.insert(i,(self.get(i) - self.get(i) % self.p))
        return item
    def __mul__(self, b):
        # checks if b is an integer and append to the list
        if isinstance(b, int):
            new_array = self.length()
            B = CauchyList(self.p)
            for i in range(new_array):
                B.content.insert(i,(self.get(i) * b % self.p))
            return B
        else:
            # if not check if p is same value and append to value
            if self.p != b.p:
                raise ValueError('p is not the same')
            new_array = self.length() + b.length() - 1
            B = CauchyList(self.p)
            minArray = min(self.length(), b.length())
            value = 0 
            for i in range(new_array):
                for j in range(minArray):
                    value = value + self.get(j) * b.get(j- minArray)
                B.content.append(value % self.p)
            return B
    def __str__(self):
        # formating for the end print statement 
        return 'p: '+ str(self.p) + '\n' + 'length: ' + str(self.length()) +'\n'+'content: ' + str(self.content)


