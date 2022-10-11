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

def myCalc(myOperators, myIntegers):
    first_op   = myOperators[0]
    second_op  = myOperators[1]
    first_int  = myIntegers[0]
    second_int = myIntegers[1]
    third_int  = myIntegers[2]

    if first_op == '*':
        int_4 = myMul(first_int, second_int) 
        if second_op == '*':
            return myMul(int_4, third_int)
        elif second_op == '/':
            return myDiv(int_4, third_int)
        elif second_op == '+':
            return myAdd(int_4, third_int)
        elif second_op == '-':
            return mySub(int_4, third_int)
        

    elif first_op == '/':
       int_5 = myDiv(first_int, second_int)
       if second_op == '*':
           return myMul(int_5, third_int)
       elif second_op == '/':
           return myDiv(int_5, third_int)
       elif second_op == '+':
           return myAdd(int_5, third_int)
       elif second_op == '-':
           mySub(int_5, third_int)

    elif second_op == '*':
       int_6 = myMul(second_int, third_int)
       if first_op == '*':
           return myMul(first_int, int_6)
       elif first_op == '/':
           return myDiv(first_int, int_6)
       elif first_op == '+':
           return myAdd(first_int, int_6)
       elif first_op == '-':
           return mySub(first_int, int_6)

    elif second_op == '/':
       int_7= myMul(second_int, third_int)
       if first_op == '*':
           return myMul(first_int, int_7)
       elif first_op == '/':
           return myDiv(first_int, int_7)
       elif first_op == '+':
           return myAdd(first_int, int_7)
       elif first_op == '-':
           return mySub(first_int, int_7)

    elif first_op == '+':
       int_8 = myAdd(first_int, second_int)
       if second_op == '+':
           return myAdd(int_8, third_int)
       elif second_op == '-':
           return mySub(int_8, third_int)

    elif first_op == '-':
       int_9 = mySub(first_int, second_int)
       if second_op == '-':
           return mySub(int_9, third_int)
       elif second_op == '+':
           return myAdd(int_9, third_int)

def displayOp(myOperators, myIntegers, myAnswer):
   print(myIntegers[0],myOperators[0],myIntegers[1],myOperators[1],myIntegers[2],'=', myAnswer)

def main():
   intList = intVal()
   OpList = operationVal()
   Answer = myCalc(OpList, intList)
   displayOp(OpList,intList,Answer)


if __name__ == '__main__':
   main()

   
 


