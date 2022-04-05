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
 

#==Main Function ==============================================================# 
def main():
  validation()

def validation():
  str = request_num()
  try:
    if str[0] == ".":
      str = "0"+str
  except IndexError:
    print(Fore.RED +"Please put in something"+Fore.WHITE)
    validation()
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

#==Convert numeral to english words============================================#
def convert(raw_num):
  num1 = ""
  num2 = ""
  try:
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
    else:
      num1 = int(raw_num) 
  except ValueError:
    print(Fore.RED +"Please enter a number"+Fore.WHITE)
    validation()

  if len(str(num1)) > 126:
    print(Fore.RED + "Sorry, this number is larger than our dictionary" +Fore.WHITE)
    validation()
  
  if num2 == "":
    if num1 < 100:    #checking to use 2_digit or 3_digit convert
      two_output = two_d_convert(num1)
      if two_output == "one":        
        print(two_output.capitalize(), "dollar")
      else:
        print(two_output.capitalize(), "dollars")
    elif num1 < 1000:
      
      print(three_d_convert(num1).capitalize(), "dollars")
    else:      #larger than 1000 input
      output_str = more_convert(num1).capitalize(), "dollars"
      print("".join(output_str))
        
  
  
  else:                      #decimal number loop

    if num1 < 100:
      two_output = two_d_convert(num1)
      if two_output == "one":        
        print(((two_output).capitalize()),"dollar and", " ".join(cents_convert(num2)))
      else:
        print(((two_output).capitalize()),"dollars and", " ".join(cents_convert(num2)))

    elif num1 < 1000:
      
      print((three_d_convert(num1).capitalize()),"dollars","and", " ".join(cents_convert(num2)))
    
    else:
      cents_output = "".join(((more_convert(num1).capitalize()),"dollars"))
      print(cents_output,"and", " ".join(cents_convert(num2)))
  
  validation()
  
#==Two digit handling =========================================================#

def two_d_convert(num):
  if num < 20:                      #validate if number fit requirement for   dictionary 1

    return (_Ones[num])    #This should able to convert number with in 1-19
        
  elif num < 100:
      tens, ones = [(num//(10**i))%10 for i in range(math.ceil(math.log(num, 10))-1,  -1, -1)]
     #Program from https://www.delftstack.com/howto/python/split-integer-into-digits-python/
      ten_in_words = _Tens[tens]  #From dictionary find tens

      if ones != 0:
        one_in_words = _Ones[ones]  #From dictionary find ones
        return " ".join((ten_in_words, one_in_words))  #prints the dollar amount
        
      else:
        return " ".join((ten_in_words))
  
  else:
    return " ".join((Fore.RED +"Not support yet"+Fore.WHITE))

#==Convert decimal to cents ===================================================#    

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


#==Three digits handling ======================================================#
def three_d_convert(num):
  raw_hundred = int(num/100)
  raw_number = num - (raw_hundred*100)
  if raw_hundred != 0:
    if raw_number != 0:
    
      hundred = (_Ones[raw_hundred], "hundred")
      return " ".join([" ".join(hundred),"and", two_d_convert(raw_number)])
    else:
      hundred = (_Ones[raw_hundred], "hundred")
      return " ".join(hundred)
  else:
    return (two_d_convert(raw_number))

    

#==Handling more than 4 digits number =========================================#
def more_convert(num):
  two_digit = ""
  string = ""
  loop_time = 0
  while num >= 100:
    last_three_numbers = int(str(num)[-3:])                #Pull out the last three digits from input                          
    num = num//1000                                        #Truncate the last three digits
    
    if loop_time != 0:      
      last_three_digits = three_d_convert(last_three_numbers)+" "+_placeholders[loop_time]+" "
    else:
      last_three_digits = three_d_convert(last_three_numbers)+" "
    if last_three_numbers == 0:
      loop_time += 1
    else:
      string = last_three_digits + string
      loop_time += 1

  else:    
    if num == 0:
      return (string.capitalize())
    else:
      two_digit = two_d_convert(num)+" "+_placeholders[loop_time]+" "
      outcome = two_digit + string
      return(outcome.capitalize())
#______MAIN_______#
print("Welcome to the number to word converter. This program is currently in development so please expect to get errors")
print("Copyright: © 2022 Forrest and Michael.")
main()
