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

_placeholders = {
    0: 'thousand',
    1: 'million',
    2: 'billion',
    3: 'trillion',
    4: 'quadrillion',
    5: 'quintillion',
    6: 'hextillion',
    7: 'septillion',
    8: 'octillion',
    9: 'nonillion',
    10: 'decillion',
    11: 'undecillion',
    12: 'duodecillion',
    13: 'tredecillion',
    14: 'quattuordecillion',
    15: 'quindecillion',
    16: 'hexdecillion',
    17: 'septendecillion',
    18: 'octodecillion',
    19: 'novemdecillion',
    20: 'vigintillion',
    21: 'unvigintillion',
    22: 'duovigintillion',
    23: 'trevigintillion',
    24: 'quattourvigintillion',
    25: 'quinvigintillion',
    26: 'hexvigintillion',
    27: 'septenvigintillion',
    28: 'octovigintillion',
    29: 'novemvigintillion',
    30: 'trigintillion',
    31: 'untrigintillion',
    32: 'duotrigintillion',
    33: 'googol',
    34: 'googolplex'
}


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
      if num == 1:
        dollar = " ".join((_Ones[num].capitalize(), "dollar"))    #Print one dollar
        
      else: 
        dollar = " ".join((_Ones[num].capitalize(), "dollars"))    #This should able to convert number with in 1-19
        
  elif num < 100:
      tens, ones = [(num//(10**i))%10 for i in range(math.ceil(math.log(num, 10))-1,  -1, -1)]
     #Program from https://www.delftstack.com/howto/python/split-integer-into-digits-python/
      ten_in_words = _Tens[tens]  #From dictionary find tens

      if ones != 0:
        one_in_words = _Ones[ones]  #From dictionary find ones
    
        dollar = " ".join((ten_in_words.capitalize(), one_in_words, "dollars"))  #prints the dollar amount
        
      else:
        dollar = " ".join((ten_in_words.capitalize(), "dollars"))
        
  elif num < 1000:    #number greater than 100
    raw_hundred = int(num/100)
    raw_number = num - (raw_hundred*100)
    hundred = (_Ones[raw_hundred], "hundred")
    dollar = " ".join(hundred)
  else:
    dollar = " ".join((Fore.RED +"Not support yet"+Fore.WHITE))



def convert(raw_num):
  num = round(float(raw_num), 2)
  if num.is_integer() == True:
    two_d_convert(num)
    print(dollar)
    validation()
  else:                      #decimal number loop
    raw_cents, raw_dollars = math.modf(num)
    two_d_convert(raw_dollars), cents_convert(round(raw_cents*100, 0))
    print(" ".join(dollar),"and", " ".join(cents))
    validation()
    
  
  
def validation():
  num_input = input("\nPlease put in amount that you would like to convert:\n$")    #This should print the code and lead   the user to type in a number
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
print("Welcome to the number to word converter. This program is currently only support number up to 100")
print("Copyright: © 2022 Forrest and Michael.")
validation()


