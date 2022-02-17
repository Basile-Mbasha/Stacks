"""
Name: Basile Mbasha
Date: February 16th,2022
Description: Assignment_02

  This program will use a stack(LIFO) to:
    . convert a given user-input expression 
    . into an infix or postfix expression based on direction entered 
    . and output the value of the converted expression

"""

#Creating a class named "Expression".
class Expression:
    
    def __init__(self):
        '''
        Description: Constructor for class "Expression".
        Input: Will be given by user 
        Output: Create lists named stack, result, digits and evaluated 
        and 1 dictionary named precedence
        (setting precedence for parenthesis and operators).
        
        '''
        self.stack = []
        self.result = []
        self.digits = []
        self.evaluated = []
        self.precedence = {'(':0, '-':1, '+':1, '*':2, '/':2, '^':3}
        self.count = 0
        
    def isEmpty(self):
        ''' 
        Description: Function to check whether stack is empty.
        Input: Null.
        Output: Returns true if stack is empty else false.
        
        '''
        return self.stack == []
    
	# Returns the number of element in stack
    def size(self) :
        return self.count
    
    def push(self,element):
        ''' 
        Description: Function to push an element on top of stack.
        Input: Element to be pushed.
        Output: Pushes the element on top of the stack.

        '''
        self.stack.append(element)
            
    def pop(self):
        ''' 
        Description: Function to pop an element from stack.
        Input: Null.
        Output: Pops an element from top of the stack and returns the value.
        
        '''
        if not self.isEmpty():
            return self.stack.pop()
        
    def peek(self):
        ''' 
        Description: Function to peek an element from stack.
        Input: Null.
        Output: Peeks the top element of the stack and returns the value.
        
        '''
        if not self.isEmpty():
            return self.stack[-1]
 

    def in_to_post(self,exp):
        ''' 
        Description: 
            Function to convert infix expression with multiple digits 
            to postfix expression. Loops through each element 
            of expression and checks for alphanumeric charecter, 
            checks for '(',')', checks precedence order in case 
            of operators and returns postfix expression.
        Input: Takes Infix expression.
        Output: Returns Postfix expression.
        exp : Expression
        
        '''
        for c in exp:
                
            if c.isalnum():
                self.digits.append(c)
                
            elif c == '(':
                    self.stack.append(c)
                    
            elif c == ')':
                self.result.append(''.join(self.digits))
                self.digits.clear()
                k = self.pop()
                while (k != '('):
                    self.result.append(k)
                    k = self.pop() 
                
            else:
                if self.digits != []:
                    self.result.append(''.join(self.digits))
                    self.digits.clear()
                while not self.isEmpty() and (self.precedence[self.peek()] >= self.precedence[c]):
                    self.result.append(self.pop())
                    
                self.push(c)
        
        if self.digits != []:
            self.result.append(''.join(self.digits))
            self.digits.clear()        
                
        while self.isEmpty() == False:
            self.result.append(self.pop())
            
        return self.result 
    
    # Check operator
    def isOperator(self, text) :
    		if (text == '+'
    			or text == '-'
    			or text == '*'
    			or text == '/'
    			or text == '^'
    			or text == '%') :
    			return True
            
    		return False
   
	 #Check operands
    def isOperands(self, text) :
	    if ((text >= '0'
				and text <= '9') or (text >= 'a'
				and text <= 'z') or (text >= 'A'
				and text <= 'Z')) :
		    return True
		
	    return False
    
	#  Converting the given postfix expression to 
	#  prefix expression
    def post_to_in(self, exp) :
        ''' 
        Description: 
            Function to convert postfix expression with multiple digits 
            to infix expression. Loops through each element 
            of expression and checks for operand and operator 
            and returns inffix expression.
        Input: Takes Postfix expression.
        Output: Returns Infix expression.
        exp : Expression
        
        '''
        
        # Get the size
        size = len(exp)

        # Create stack object
        s = Expression()
		
		# Some useful variables which will be used
		# to store current result
        auxiliary = ""
		# boolean to check validity 
        isValid = True
		# Initializing index to zero
        i = 0
		
        while (i < size and isValid) :
			
            #  Check whether given postfix location
			#  at [i] is an operator or not
            if (self.isOperator(exp[i])) :
                
				#  When operator exist
				#  Check that two operands exist or not
                if (s.size() > 1) :
                    auxiliary = s.pop()
                    auxiliary = s.pop() + auxiliary
                    auxiliary = exp[i] + auxiliary
                    s.push(auxiliary)
				
                else:	
                    isValid = False
					
            elif (self.isOperands(exp[i])) :
				# When get valid operands
                auxiliary = exp[i]
                s.push(auxiliary)
            else :
				# Invalid operands or operator
                isValid = False

            i += 1
		
        if (isValid == False) :
			# When have something wrong
            print("Invalid postfix : ", exp)
	
        else :
			# Display calculated result
            return s.pop()

        
    def evaluate(self,exp):
        '''
        Description: Function evaluates the Expression.
        Input: Expression.
        Output: Evaluated value of the expression.
        
        '''
        for i in exp:
            
            if i.isalnum():
                self.evaluated.append(i)
            else:
                a = self.evaluated.pop()
                b = self.evaluated.pop()
                self.evaluated.append(str(eval(b+i+a)))
        return (self.evaluated[0])        
    

def main():
    
    #Creating an object char or 'character' of class "Expression".               
    char = Expression()

    #Prompting the user for input --> expression. 
    user_input = str(input("Enter the expression to convert: "))


    # coding_input_test = (23+41+7*8)*2 
    
    
    #Getting string casted user input --> direction of convertion.
    direction = str(input("Enter the direction (0 for infix and 1 for postfix): "))

    #Checking for the value in direction (0 or 1)
    for value in direction:
        if (value == "0"):
            print("The Infix Expression is:",user_input)
            j = (char.in_to_post(user_input))
            print("The Postfix Expression is:",''.join(j))
            print("The Value of the converted Expression is:",char.evaluate(j))
            break
        elif (value == "1"):
            print("The Postfix Expression is:",user_input)
            j1 = (char.post_to_in(user_input))
            print("The Infix Expression is:",j1)
            #print("The Value of the converted Expression is: ",char.evaluate(j1))
            break  
        else:
            print("Invalid user input")
            break
            
if __name__ == "__main__": main()        



