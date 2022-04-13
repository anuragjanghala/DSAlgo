# RPN CAL

# operators : +, -, *, /, sqrt()
# DS-> stack : []

# all inputs will be vaild no ERROR handling

# input = "6 8 4 + 3 2 + - *"



###################### Code Implementation #####################

###### stack class

import math

class Stack:
    def __init__(self):
        self.stack=[] # initialize the empty stack
    
    def add_to_stack(self, input):
        self.stack.append(input) # it will add value to the top of the stack
        
    def pop(self):
        self.stack.pop() # it will delete the last value from the stack

    def computation(self, opr): # [5 8]
        # hashmap = {'+': add(), ...}
        # res = []
            if opr == '+':
                res = self.stack[-2]+self.stack[-1] # 5 11 + = 16  
            elif opr == '-': # [5 3 -]=2 [3 5 -]=-2
                res = self.stack[-2]-self.stack[-1]
            elif opr == '*':
                res= self.stack[-2]*self.stack[-1]
            elif opr == '/': 
                res = self.stack[-2]/self.stack[-1]
            else:
                res = math.sqrt(self.stack[-1])
            
            if opr != 'sqrt':
                self.stack.pop()
            self.stack.pop()
            self.add_to_stack(res)
                
    def look_up(self):
        if len(self.stack) == 1:
            return self.stack[0]

####### input function
input = "5 4 2 * 3 + + sqrt" 
# input = "3.12 4 + 2 *"

def input_funtion(input):
    input_list = list(input.split(' '))
    print(input_list) # ['5', '4', '2', '*', '3', '+', '+', 'sqrt']
    
    opr = ['+','-','*','/','sqrt']
    
    obj = Stack()
    
    for i in input_list:
        
        # if operator or if its an integer
        if i in opr:
           obj.computation(i) 
        else:
            obj.add_to_stack(float(i))
            #obj.look_up()
            
    result = obj.look_up()
    return result
            
result = input_funtion(input)
print(result)
    
# stack = [6 12 5 ]