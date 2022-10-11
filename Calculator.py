def myAdd(num1,num2):
    return num1 + num2

def mySub(num1, num2):
    return num1 - num2

def myMul(num1, num2):
    return num1*num2

def myDiv(num1, num2):
    return num1//num2

def intVal():   
   myIntegers = []
 
   integer_number = 4
   while len(myIntegers) < integer_number:
       try:   
           int_1 = int(input('Enter the first integer for your calculation: '))
       except ValueError:
           print('Please enter an Integer')
           continue
       else:
        print('You entered: ', int_1)
       myIntegers.append(int_1)
       break
   while len(myIntegers) < integer_number:  
       try:   
           int_2 = int(input('Enter the second integer for your calculation: '))   
       except ValueError:
           print('Please enter an Integer')
           continue
       else:
           print('You entered: ', int_2)
       myIntegers.append(int_2)
       break
   while len(myIntegers) < integer_number:
       try:   
           int_3 = int(input('Enter the third integer for your calculation: '))   
       except ValueError:
           print('Please enter an Integer')
           continue
       else:
           print('You entered: ', int_3)
       myIntegers.append(int_3)
       break
   
   print('Your inputs for the calculator are: ')
   print(myIntegers)
   return myIntegers
   
def operationVal():
   myOperators = []
   myOplist = [ '*' , '/' , '+' , '-' ]
 
   print('Enter the operators that you would like to use: \n"*" for Multiplication\n"/" for Division\n"+" for Addition\n"-" for Subtration')
   
   operator_1 = input("Please enter the first operator: ")
   while operator_1 not in myOplist:
       print('Please enter a valid operator')
       operator_1 = input("Please enter the first operator: ")
 
   print('You entered', operator_1)
   myOperators.append(operator_1)
   
   operator_2 = input('Enter the second operator: ')
   while operator_2 not in myOplist:
       print('Please enter a valid operator')
       operator_2 = input('Enter the second operator: ')
 
   print('You entered', operator_2)
   myOperators.append(operator_2)
  
   return myOperators


  


