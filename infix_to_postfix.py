#Why Postfix:-
#Compiler either scans an expression from either left to right or right to left
#so for infix expression it has to scan same string multiple times making it very in-efficient...
#So it is better to convert the expression to Postfix form.

#Rules:-
# highest priority to paraenthesis
# expoenetial (right to left)
# multipication/division (left to tight)
# addition/substaction (left to right)

#Algo:-
#	stack  = []
#	d = {'+':1, '-':1, '*':2, '/':2, '^':3}
#	for every char c in infix:
#		if the c is '('
#			stackPush
#		else if c is ')'
#			while stack not Empty and stack[top] != '('
#				do
#				stackPop and append to output string
#			if stack not empty and stack[top] != '('
#				invalid string
#			stack pop the left '('
#		else if c is operator
#			while stack not empty and stack[top] has high value than c
#				do
#				append stack[top] to output
#				stackPop
#			append the current operator c
#
#		else if c is alhanumeric
#			directly append to output
#		else
#			invalid character... 

def has_valid_parathesis(infix):
	
	stack = []
	for i in infix:
		if i == '(':
			stack.append(i)
		elif i == ')':
			stack.pop()
	if not stack:
		return True 
	else:
		return False

def higher_precedence(operator1, operator2):

	#key: value for operator and it's precedence value...
	try:
		d = {'+':1, '-':1, '*':2, '/':2, '^':3}
		return True if d[operator1] >= d[operator2] else False
	except KeyError:
		return False

def infix_to_postfix(infix):

	postfix = ""
	stack = []
	operators = "^*+-/%()"
	
	for i in infix:
		
		if i in operators:
		
			if i == '(':
				stack.append(i)
			elif i == ')':
				#if character is operator first check stack is non-empty and until '(' comes 
				while stack and stack[-1] != '(':
					postfix += stack[-1]
					stack.pop()
				if stack and stack[-1] != '(':
					return "Invalid set of paranthesis"
				else:
					#pop the '(' character...
					stack.pop()
			else:
				#if stack not empty and 
				#check if precendence of current of operator is less than stack[top] then append stack[top] to postfix and pop it
				#until stack becomes empty or precendence of current operator becomes greater than stack[top] 
				while stack and higher_precedence(stack[-1], i):
					postfix += stack[-1]
					stack.pop()	
				#otherwise just push operator to the stack
				stack.append(i)		
					
		elif str(i).isalnum() :
			#if character is a operand then just append it, because sequence of the operand will be as same as in infix... 
			postfix += i 
		else:
			return ("Invalid infix expression because of %s character" % i)
	while stack:
		#pop all the remaining elements of stack and append it to postfix 
		postfix += stack[-1]
		stack.pop()
	return postfix
	
	
def main():

	infix_string = input("Enter infix expression\n")
	if has_valid_parathesis(infix_string):
		print ("Infix   Expression ==> %s" % infix_string)
		print ("Postfix Expression ==> %s" %infix_to_postfix(infix_string))
	else:
		print ("Invalid expression due to inappropirate set of parantheses")
	
if __name__ == "__main__":
	main()
	

