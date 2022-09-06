def numbers_range(number: int):
  #   write your code here

  result = []

  for i in range(0, int(number)+1):
    result.append(i)
    
  output = str(result).strip('[]').replace(',', '')
  return output