#______________________imports___________________#
import math
import colorama
from colorama import Fore
from data import _Ones, _Tens, _placeholders
#_____________DEFINE___________#





error =("not supporting yet")

#__________Function___________#
def cents_convert(cent):
  global cents
  if cent < 20:                      #validate if number fit requirement for   dictionary 1
      if cent == 1:
        cents = (_Ones[cent], "cent")    #Print one dollar
      else: 
        cents = (_Ones[cent], "cents")    #This should able to convert number with in 1-19
  elif cent < 100:
      ten_cents, single_cents = [(cent//(10**i))%10 for i in range(math.ceil(math.log(cent, 10))-1,  -1, -1)]
     #Program from https://www.delftstack.com/howto/python/split-integer-into-digits-python/
      ten_cents_in_words = _Tens[ten_cents]  #From dictionary find tens

      if single_cents != 0:
        single_cents_in_words = _Ones[single_cents]  #From dictionary find single_cents
    
        cents = (ten_cents_in_words, single_cents_in_words, "cents")  #prints the dollar amount
      else:
        cents = (ten_cents_in_words, "cents")
  else:    #number greater than 100
      cents = (Fore.RED +"There is an error"+Fore.WHITE)


def two_d_convert(num):
  global dollar
  if num < 20:                      #validate if number fit requirement for   dictionary 1
      if is_num == 1:
        dollar = " ".join((_Ones[num], "dollar"))    #Print one dollar
        
      else: 
        dollar = " ".join((_Ones[num], "dollars"))    #This should able to convert number with in 1-19
        
  elif num < 100:
      tens, ones = [(num//(10**i))%10 for i in range(math.ceil(math.log(num, 10))-1,  -1, -1)]
     #Program from https://www.delftstack.com/howto/python/split-integer-into-digits-python/
      ten_in_words = _Tens[tens]  #From dictionary find tens

      if ones != 0:
        one_in_words = _Ones[ones]  #From dictionary find ones
        dollar = " ".join((ten_in_words, one_in_words, "dollars"))  #prints the dollar amount
        
      else:
        dollar = " ".join((ten_in_words, "dollars"))
  
  else:
    dollar = " ".join((Fore.RED +"Not support yet"+Fore.WHITE))

def three_d_convert(num):
  global join_hundred
  raw_hundred = int(num/100)
  raw_number = num - (raw_hundred*100)
  if raw_number != 0:
    two_d_convert(raw_number)
    hundred = (_Ones[raw_hundred], "hundred")
    join_hundred = " ".join([" ".join(hundred),"and", dollar])
  else:
    hundred = (_Ones[raw_hundred], "hundred")
    join_hundred =" ".join(hundred)
    


def convert(raw_num):
  num = round(float(raw_num), 2)
  if num.is_integer() == True:
    if num < 100:    #checking to use 2_digit or 3_digit convert
      two_d_convert(num)
      print(dollar.capitalize())
      validation()
    elif num < 1000:
      three_d_convert(num)
      print(join_hundred.capitalize())
      validation()
    else:      #larger than 1000 input
      number = "storage"
      first = "storgae"
      string = " "
      loop_time = 0
      while num > 100:
        last_three_numbers = int(abs(num) % 1000)
        num = num/1000
        three_d_convert(last_three_numbers)
        
        number = join_hundred.rsplit(' ', 1)[0]+" "+_placeholders[loop_time]
        
        string = number + string 
        loop_time += 1
        
      else: 
        two_d_convert(int(num))
        first = dollar.rsplit(' ', 1)[0]+" "+_placeholders[loop_time]
        outcome = first + string
        print(outcome)
        
  
  
  else:                      #decimal number loop
    raw_cents, raw_dollars = math.modf(num)
    if num < 100:
      two_d_convert(raw_dollars), cents_convert(round(raw_cents*100, 0))
      print((dollar.capitalize()),"and", " ".join(cents))
      validation()

    elif num < 1000:
      three_d_convert(raw_dollars), cents_convert(round(raw_cents*100, 0))
      print((join_hundred.capitalize()),"and", " ".join(cents))
      validation()
    
    else:
      print((Fore.RED +"Not support yet"+Fore.WHITE).capitalize())
      validation()
    
  
  
def validation():
  global is_num
  num_input = input("\nPlease put in a number amount that you would like to convert:\n$")    #This should print the code and lead   the user to type in a number
  try:
    is_num = float(num_input)
    
    
    
  except ValueError:
    print(Fore.RED +"Please put in a VALID number"+Fore.WHITE)
    validation()

  if is_num > -1:
    convert(is_num)
  else:  
    print(Fore.RED +"Please enter a positive number to convert"+Fore.WHITE)
    validation()

#______MAIN_______#
print("Welcome to the number to word converter. This program is currently only support amount up to $999.99")
print("Copyright: © 2022 Forrest and Michael.")
validation()


