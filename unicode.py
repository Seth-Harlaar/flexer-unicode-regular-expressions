import re
import math
# get the hex representation of a single unicode value
def make_hex_single(u_input):
  hex_input = u_input.encode('utf-8').hex()
  hex_result = ''
  for index in range(0, len(hex_input), 2):
    hex_result = hex_result + '\\x' + (hex_input[index: index + 2])
  return hex_result


def make_proper_uni(char_input):
  length = len(char_input)
  char = char_input
  char = char.zfill(8)
  char = chr(int(char, 16))

  return char
  

alpha_char = []
punc_char = []
symb_char = []


# general categories
L = ['Lu', 'Ll', 'Lt', 'Lm', 'Lo']
M = ['Mn', 'Mc', 'Me']

P = ['Pc', 'Pd', 'Ps', 'Pe', 'Pi', 'Pf', 'Po']

S = ['Sm', 'Sc', 'Sk', 'So']

# parse the unicdoe file to get all the different categories

unicode_lines = open('all_unicode_chars.txt', 'r')

for line in unicode_lines:
  line_parts = line.split(';')
  g_cat = line_parts[2]

  char_code = line_parts[0]  

  unicode_char = make_proper_uni(char_code)

  # exclude surrogates
  if( re.search(r'[\uD800-\uDFFF]', unicode_char) == None ):
    hex_code = make_hex_single(unicode_char)

    if(g_cat in L or g_cat in M):
      alpha_char.append(hex_code)
    
    if(g_cat in P):
      punc_char.append(hex_code)

    if(g_cat in S):
      symb_char.append(hex_code)



print('Alpha Characters:')
#print(alpha_char)
print('Punctuation Characters:')
#print(punc_char)
print('Symbol Characters:')
#print(symb_char)


print(punc_char[0] + '|' + punc_char[1])

lines = []


def make_hex_string(hex_list, prefix, title):
  print('make hex string')
  max_length = 1900
  hex_strings = []
  temp_string = ''
  i = 0
  j = 1  
  
  # make a new temp string
  temp_string = prefix + '_' + str(j) + '          '

  while( i < len(hex_list) ):
    # add hex code to temp string
    temp_string = temp_string + hex_list[i]
    
    # check if length is to large, if so make new one and fill it up
    if( len(temp_string) >= 1900 ):
      hex_strings.append(temp_string)
      j += 1
      temp_string = prefix + '_' + str(j) + '          '

    # if its not too big, add | so that more hex codes can be added
    else:
      temp_string = temp_string + '|'

    i += 1

  final_string = title + '          '

  j = 1

  for string in hex_strings:
    print(string)
    final_string = final_string + '{' + prefix + '_' + str(j) + '}'
    j += 1

  print(final_string)




make_hex_string(punc_char, 'PC', 'PUNC_CHARS')
