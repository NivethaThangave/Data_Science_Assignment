def encode(encoded_input):
  print("Passing the encoded Input string: " + encoded_input )
  encoded_output = ''
  data = ''
  encoded_input_check = any(i.isdigit() for i in encoded_input)
  print("Checking the Encoded_input value is an empty or it contains any integer values...")
  if(encoded_input == " "):
      print("Your Input string is empty, Please enter a proper non empty string value")
      return ""
  elif(encoded_input_check == True):
      print("Your Input contains a Numeric value, Please change it")
      return ""
  else:
   print("Hurray!!! your Encoded_Input is not an empty and doesn't contain any integer value")   
   print("Creating a For-loop with range 0 to the length of the given encoded_input in order to get all the given encoded_input string as one by one character.")
  for i in range(0,len(encoded_input)):
   if (data==''):
      count = 1
   elif (encoded_input[i]==data):
      count = count + 1
   else:
      encoded_output = encoded_output+str(count) + data
      count = 1
   data = encoded_input[i]
  encoded_output = encoded_output+str(count)+data
  return("Encoded_Output value is "+ encoded_output)

print (encode("aaaabbbbccccdddd"))
