# A python program that translates phrases into morse code
# Inspired by the first chapter of Charles Petzold's Code

# PSEUDO CODE
# receive input from user
# iterate over user statement
# print to terminal corresponding morse code character

# store morse code translations in a dictionary
morse = {
  "a":"*-",
  "b":"-***",
  "c":"-*-*",
  "d":"-**",
  "e":"*",
  "f":"**-*",
  "g":"--*",
  "h":"****",
  "i":"**",
  "j":"*---",
  "k":"-*-",
  "l":"*-**",
  "m":"--",
  "n":"-*",
  "o":"---",
  "p":"*--*",
  "q":"--*-",
  "r":"*-*",
  "s":"***",
  "t":"-",
  "u":"**-",
  "v":"***-",
  "w":"*--",
  "x":"-**-",
  "y":"-*--",
  "z":"--**",
  "1":"*----",
  "2":"**---",
  "3":"***--",
  "4":"****-",
  "5":"*****",
  "6":"-****",
  "7":"--***",
  "8":"---**",
  "9":"----*",
  "0":"-----",
  " ":"  "
}

# ask user for initial phrase to translate
init_phrase = input("Enter a phrase or word to translate: ").toLowerCase()

# iterate over phrase and find corresponding morse code translation
for char in init_phrase:
  print(morse[char], end=" ")
print()
