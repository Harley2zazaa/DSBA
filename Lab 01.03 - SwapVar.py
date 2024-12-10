"""SwapVar"""
def convert_string_to_tuples(text_in):
  """SSSSS"""
  values = text_in.strip('()').split(', ')
  return tuple(map(float, values))

LAONGDAL = convert_string_to_tuples(input())
print(LAONGDAL[::-1])
