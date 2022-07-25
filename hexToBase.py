#-------------------------------------------------------------------------------------------------------
# The cryptopals - crypto challenges |
#------------------------------------#
# @title Set 1 Challenge 1

# @author Maka
# @notice a return to these after some years, a little older and hopefully wiser
#-

#-- an in-built solution: no imports and does the same thing
# def hex2base64(hex_string):
#   cache = bytes.fromhex(hex_string)
#   return cache.decode('ascii')
#-

#-- an i-built solution
# ->
# unchecksum
def uncheck(_str):
  chars = {
    'A':'a', 'B':'b', 'C':'c', 'D':'d', 'E':'e', 'F':'f',
    'G':'g', 'H':'h', 'I':'i', 'J':'j', 'K':'k', 'L':'l',
    'M':'m', 'N':'n', 'O':'o', 'P':'p', 'Q':'q', 'R':'r',
    'S':'s', 'T':'t', 'U':'u', 'V':'v', 'W':'w', 'X':'x',
    'Y':'y','Z':'z'
  }  
  buffer = ''
  for i in _str:
    for k in chars:
      if i == k:
        i = chars[i]
    buffer += i
  return buffer

# hex to binary mapping 
def _h2b(_hex):
  bin_ = ''
  bin_map = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111', 
    '8': '1000', '9': '1001', 'a': '1010', 'b': '1011', 'c': '1100', 'd': '1101', 'e': '1110', 'f': '1111'
  } 
  for i in uncheck(_hex):
    bin_ += bin_map[i]
  return bin_

# binary to decimal
def _b2d(_bin):
  dec = 0
  for n in _bin:
    dec = (dec * 2) + int(n)
  return dec

# binary to base64
def _b2b(_bin):
  chunks = []
  start = 0
  stop = len(_bin)
  step = 6
  for bits in range(start, stop, step):
    chunks += [_bin[bits:bits+6]]
  last_chunk = chunks[len(chunks) -1]
  pad = (6 - len(last_chunk))
  last_chunk += pad * '0'
  
  upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  lower = uncheck(upper) # 'abcdefghijklmnopqrstuvwxyz'
  digits = '0123456789'
  b64_alpha = f'{upper}{lower}{digits}+/'

  base = ''
  for bits in chunks:
    base += (b64_alpha[_b2d(bits)])
  base += int(pad / 2) * '='
  return(base)

#- - external function
def hex2b64(_hex):
  return _b2b(_h2b(_hex))
# - - - - 

#-- main
# Set 1 Challenge 1
#   Convert hex to base64
#   The string:
#     49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
#   Should produce:
#    SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
def main():
  s = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
  v = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
  base = hex2b64(s)
  r = f'[+] {v}' if base == v else f'[!] {base}'

  print(r)

if __name__ == '__main__':
  main()
#-

#- 1 love
