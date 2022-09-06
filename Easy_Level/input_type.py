def input_type(value):
  # write your code here
  num = ['1', '2', '3', '4', '5' ,'6' , '7', '8', '9', '0']
  if value.count('.') > 0:
    return "double"
  elif value[0] in num and value.count('.') == 0:
    return "integer"
  else:
    return "string"