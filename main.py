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
def convert(num):
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
  else:
    print("Not support yet")
  
  
def validation():
  num_input = input("Please put in amount that you would like to convert:\n")    #This should print the code and lead   the user to type in a number
  try:
    is_num = float(num_input)
    
  except ValueError:
    print(Fore.RED +"Please put in a VALID number")
    print(Fore.WHITE)
    validation()

  if is_num > -1:
    convert(is_num)
  else:  
    print("Please enter a positive number to convert")

#______MAIN_______#
validation()


