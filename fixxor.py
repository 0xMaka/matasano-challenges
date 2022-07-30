#-------------------------------------------------------------------------------------------------------
# The cryptopals - crypto challenges |
#------------------------------------#
# @title Set 1 Challenge 2

# @author Maka

from hexToBase import h2b # our own imports are ok

#-- housekeeping
# let's flip the bit_map from before
bit_map = {
  '0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111', 
  '8': '1000', '9': '1001', 'a': '1010', 'b': '1011', 'c': '1100', 'd': '1101', 'e': '1110', 'f': '1111'
}

class Cache(dict):
  def __init__(self):
    self = dict()
  def add(self, k, v):
    self[k] = v

def flip_map(_bit_map):
  hex_map = Cache()
  for i in _bit_map:
    hex_map.add(_bit_map[i], i)
  return hex_map

HEX_MAP = flip_map(bit_map)

# will be chunking for a second time, so can have a function for that
def chunk(_bin, _step):
  chunks = []
  start, stop, step = 0, len(_bin), _step
  for bits in range(start, stop, step):
    chunks += [_bin[bits:bits+step]]
  return chunks
 
#- end houskeeping

#-- core functions
# this is a xor.. yes it is.
def xor(x,y):
  assert len(x) == len(y), 'len x and y must be equal'
  str_ = ''
  for i in range(len(x)):
    bool_ = 0 if x[i] == y[i] else 1
    str_ += str(bool_)
  return str_

# bin to hex mapping 
def b2h(_bin):
  chunks = chunk(_bin, 4) 
  hex_ = ''
  for i in chunks:
    hex_ += HEX_MAP[i]
  return hex_

# - - - caller
def fixxor(_hex0, _hex1):
 return b2h(xor(h2b(_hex0), h2b(_hex1)))
# - -

# Set 1 Challenge 2 Fixed XOR
#   Write a function that takes two equal-length buffers and produces their XOR combination.
#
# If your function works properly, then when you feed it the string:
#   '1c0111001f010100061a024b53535009181c'
# ... after hex decoding, and when XOR'd against:
#   '686974207468652062756c6c277320657965'
# ... should produce:
#   '746865206b696420646f6e277420706c6179'
def main():
  x = '1c0111001f010100061a024b53535009181c'
  y = '686974207468652062756c6c277320657965'
  z = '746865206b696420646f6e277420706c6179'

  string = (fixxor(x,y))
  r = f'[+] {string}' if string == z else f'[!] {string}'
  print(r)

if __name__ == '__main__':
  main()
#-

#- 1 love
