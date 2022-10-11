def myCalc(myOperators, myIntegers):
    first_op   = myOperators[0]
    second_op  = myOperators[1]
    first_int  = myIntegers[0]
    second_int = myIntegers[1]
    third_int  = myIntegers[2]
    
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
   



