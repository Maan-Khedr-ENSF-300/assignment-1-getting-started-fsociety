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
