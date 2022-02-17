# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 16:49:52 2022

@author: Basile100
"""

#  Python 3 program for
#  Postfix to prefix conversion

#           Stack class                  #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Stack :
	def __init__(self, data, top) :
		self.data = data
		self.next = top
	

class MyStack :
	def __init__(self) :
		self.top = None
		self.count = 0
	
	#  Returns the number of element in stack
	def size(self) :
		return self.count
	
	def isEmpty(self) :
		if (self.size() > 0) :
			return False
		else :
			return True
		
	
	#  Add a new element in stack
	def push(self, data) :
		#  Make a new stack node
		#  And set as top
		self.top = Stack(data, self.top)
		#  Increase node value
		self.count += 1
	
	#  Add a top element in stack
	def pop(self) :
		temp = ""
		if (self.isEmpty() == False) :
			#  Get remove top value
			temp = self.top.data
			self.top = self.top.next
			#  Reduce size
			self.count -= 1
		
		return temp
	
	#  Used to get top element of stack
	def peek(self) :
		if (not self.isEmpty()) :
			return self.top.data
		else :
			return ""
        
		
#	     Infix - Postfix Conversion             #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Conversion :
	#  Check operator
	def isOperator(self, text) :
		if (text == '+'
			or text == '-'
			or text == '*'
			or text == '/'
			or text == '^'
			or text == '%') :
			return True
		
		return False
	
	#  Check operands
	def isOperands(self, text) :
		if ((text >= '0'
				and text <= '9') or (text >= 'a'
				and text <= 'z') or (text >= 'A'
				and text <= 'Z')) :
			return True
		
		return False
	
	#  Converting the given postfix expression to 
	#  prefix expression
	def postfixToPrefix(self, postfix) :
		#  Get the size
		size = len(postfix)
		#  Create stack object
		s = MyStack()
		#  Some useful variables which is using 
		#  of to storing current result
		auxiliary = ""
		isValid = True
		i = 0
		while (i < size and isValid) :
			#  Check whether given postfix location
			#  at [i] is an operator or not
			if (self.isOperator(postfix[i])) :
				#  When operator exist
				#  Check that two operands exist or not
				if (s.size() > 1) :
					auxiliary = s.pop()
					auxiliary = s.pop() + auxiliary
					auxiliary = postfix[i] + auxiliary
					s.push(auxiliary)
				else :
					isValid = False
				
			elif (self.isOperands(postfix[i])) :
				#  When get valid operands
				auxiliary = postfix[i]
				s.push(auxiliary)
			else :
				#  Invalid operands or operator
				isValid = False
			
			i += 1
		
		if (isValid == False) :
			#  When have something wrong
			print("Invalid postfix : ", postfix)
		else :
			#  Display calculated result
			print(" Postfix : ", postfix)
			print(" Prefix  : ", s.pop())
		
	
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def main() :
	task = Conversion()
	postfix = "ab+c*ef+g/+"
	task.postfixToPrefix(postfix)
	postfix = "abc*de-/+"
	task.postfixToPrefix(postfix)

if __name__ == "__main__": main()

