#______________________imports___________________#
import math
from colorama import Fore
from data import _Ones, _Tens, _placeholders
#_____________DEFINE___________#

error =("not supporting yet")

#__________Function___________#
def request_num():
  num_input = input("\nPlease put in a number amount that you would like to convert:\n$")
  return num_input
#=========================================  
def validation():
  str = request_num()
  try:                #try if input number
    float(str)
    
    
    
  except ValueError:
    print(Fore.RED +"Please put in a VALID number"+Fore.WHITE)
    validation()
  if float(str) >= 0:      #Try if numeber bigger or equal 0
    convert(str)
  else:  
    print(Fore.RED +"Please enter a positive number to convert"+Fore.WHITE)
    validation()

#===========================================================#
def convert(raw_num):
  num1 = ""
  num2 = ""
  if "." in raw_num:
    split_num = raw_num.split(".")
    num1, num2 = split_num 
    num1 = int(num1)
    num2 = num2[0:3]
    num2 = int(num2)/(10**len(num2))
    #print(num2)
    num2 = round(num2, 2)
    #print(num2)
    num2 = num2*100
    #print(split_num)
    
    if num2 == 100:
      num1 = num1 + 1
      num2 = ""
      print(num1)
      print(num2)
    else:
      print(num1)
      print(num2)
  else:
    num1 = int(raw_num) 
  
  if num2 == "":
    if num1 < 100:    #checking to use 2_digit or 3_digit convert
      
      print(two_d_convert(num1).capitalize())
    elif num1 < 1000:
      
      print(three_d_convert(num1).capitalize())
    else:      #larger than 1000 input
      print(more_convert(num1).capitalize())
        
  
  
  else:                      #decimal number loop

    if num1 < 100:
      print((two_d_convert(num1).capitalize()),"and", " ".join(cents_convert(num2)))

    elif num1 < 1000:
      
      print((three_d_convert(num1).capitalize()),"and", " ".join(cents_convert(num2)))
    
    else:
      print((more_convert(num1).capitalize()),"and", " ".join(cents_convert(num2)))
  
  
  validation()
#==========================================================
def two_d_convert(num):
  if num < 20:                      #validate if number fit requirement for   dictionary 1
      if num == 1:
        return " ".join((_Ones[num], "dollar"))    #Print one dollar
        
      else: 
        return " ".join((_Ones[num], "dollars"))    #This should able to convert number with in 1-19
        
  elif num < 100:
      tens, ones = [(num//(10**i))%10 for i in range(math.ceil(math.log(num, 10))-1,  -1, -1)]
     #Program from https://www.delftstack.com/howto/python/split-integer-into-digits-python/
      ten_in_words = _Tens[tens]  #From dictionary find tens

      if ones != 0:
        one_in_words = _Ones[ones]  #From dictionary find ones
        return " ".join((ten_in_words, one_in_words, "dollars"))  #prints the dollar amount
        
      else:
        return " ".join((ten_in_words, "dollars"))
  
  else:
    return " ".join((Fore.RED +"Not support yet"+Fore.WHITE))
#========================================================
def cents_convert(cent):
  if cent < 20:                      #validate if number fit requirement for   dictionary 1
      if cent == 1:
        return (_Ones[cent], "cent")    #Print one dollar
      else: 
        return (_Ones[cent], "cents")    #This should able to convert number with in 1-19
  elif cent < 100:
      ten_cents, single_cents = [(cent//(10**i))%10 for i in range(math.ceil(math.log(cent, 10))-1,  -1, -1)]
     #Program from https://www.delftstack.com/howto/python/split-integer-into-digits-python/
      ten_cents_in_words = _Tens[ten_cents]  #From dictionary find tens

      if single_cents != 0:
        single_cents_in_words = _Ones[single_cents]  #From dictionary find single_cents
    
        return (ten_cents_in_words, single_cents_in_words, "cents")  #prints the dollar amount
      else:
        return (ten_cents_in_words, "cents")
  else:    #number greater than 100
      return (Fore.RED +"There is an error"+Fore.WHITE)

#=====================================================

def three_d_convert(num):
  raw_hundred = int(num/100)
  raw_number = num - (raw_hundred*100)
  if raw_number != 0:
    
    hundred = (_Ones[raw_hundred], "hundred")
    return " ".join([" ".join(hundred),"and", two_d_convert(raw_number)])
  else:
    hundred = (_Ones[raw_hundred], "hundred")
    return " ".join(hundred)
#====================================================
def more_convert(num):
  number = ""
  first = ""
  string = ""
  loop_time = 0
  while num >= 100:
    last_three_numbers = int(str(num)[-3:])
    print(last_three_numbers)
    num = num//1000
    
        
    number =       three_d_convert(last_three_numbers).rsplit(' ', 1)[0]+" "+_placeholders[loop_time]+" "

    if last_three_numbers == 0:
      loop_time += 1
    else:
      string = number + string 
      loop_time += 1

  else:    
    if num == 0:
      return (string.capitalize())
    else:
      first = two_d_convert(num).rsplit(' ', 1)[0]+" "+_placeholders[loop_time]+" "
      outcome = first + string
      return(outcome.capitalize())
#______MAIN_______#
print("Welcome to the number to word converter. This program is currently only support amount up to $999.99")
print("Copyright: © 2022 Forrest and Michael.")
validation()
