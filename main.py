#______________________imports___________________#
import math
import colorama
from colorama import Fore
#_____________DEFINE___________#


_Ones = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    0: 'zero'
}

_Tens = {
    2: 'twenty',
    3: 'thirty',
    4: 'forty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety'
}

error =("not supporting yet")

#__________Function___________#
def cents_convert(cent):
  if cent < 20:                      #validate if number fit requirement for   dictionary 1
      if cent == 1:
        print(_Ones[cent].capitalize(), "cent")    #Print one dollar
        validation()
      else: 
        print(_Ones[cent].capitalize(), "cents")    #This should able to convert number with in 1-19
        validation()
  elif cent < 100:
      ten_cents, single_cents = [(cent//(10**i))%10 for i in range(math.ceil(math.log(cent, 10))-1,  -1, -1)]
     #Program from https://www.delftstack.com/howto/python/split-integer-into-digits-python/
      ten_cents_in_words = _Tens[ten_cents]  #From dictionary find tens

      if single_cents != 0:
        single_cents_in_words = _Ones[single_cents]  #From dictionary find single_cents
    
        print(ten_cents_in_words.capitalize(), single_cents_in_words, "cents")  #prints the dollar amount
        validation()
      else:
        print(ten_cents_in_words.capitalize(), "cents")
        validation()
  else:    #number greater than 100
      print(Fore.RED +"Not support yet"+Fore.WHITE)
      validation()


def two_d_convert(num):
  if num < 20:                      #validate if number fit requirement for   dictionary 1
      if num == 1:
        print(_Ones[num].capitalize(), "dollar")    #Print one dollar
        
      else: 
        print(_Ones[num].capitalize(), "dollars")    #This should able to convert number with in 1-19
        
  elif num < 100:
      tens, ones = [(num//(10**i))%10 for i in range(math.ceil(math.log(num, 10))-1,  -1, -1)]
     #Program from https://www.delftstack.com/howto/python/split-integer-into-digits-python/
      ten_in_words = _Tens[tens]  #From dictionary find tens

      if ones != 0:
        one_in_words = _Ones[ones]  #From dictionary find ones
    
        print(ten_in_words.capitalize(), one_in_words, "dollars")  #prints the dollar amount
        
      else:
        print(ten_in_words.capitalize(), "dollars")
        
  else:    #number greater than 100
      print(Fore.RED +"Not support yet"+Fore.WHITE)
      



def convert(raw_num):
  num = round(float(raw_num), 2)
  if num.is_integer() == True:
    two_d_convert(num)
  else:                      #decimal number loop
    cents, dollars = math.modf(num)
    print("Cents:", round(cents, 2))
    print("Dollars:", dollars)
    two_d_convert(dollars)
    cents_convert(round(cents, 2)*100)
    
  
  
def validation():
  num_input = input("\nPlease put in amount that you would like to convert:\n")    #This should print the code and lead   the user to type in a number
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
print("Welcome to the number to word converter.")
validation()


