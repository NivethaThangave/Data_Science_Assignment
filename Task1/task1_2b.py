def encode(encoded_input):
  print("Passing the encoded Input string: " + encoded_input )
  encoded_output = ''
  data = ''
  # Checking the input string containing any integer value or not by using isdigit() function
  encoded_input_check = any(i.isdigit() for i in encoded_input)
  print("Checking the Encoded_input value is an empty or it contains any integer values...")
  # checking the input string is empty or not
  if(encoded_input == " "):
      print("Your Input string is empty, Please enter a proper non empty string value")
      return ""
  # if the inout string doesnot contain any integer value then pass the below condition 
  elif(encoded_input_check == True):
      print("Your Input contains a Numeric value, Please change it")
      return ""
  # if the above two condtion not satisfied then your input string is perfect for encryption.
  else:
   print("Hurray!!! your Encoded_Input is not an empty and doesn't contain any integer value")   
   print("Creating a For-loop with range 0 to the length of the given encoded_input in order to get all the given encoded_input string as one by one character.")
  for i in range(0,len(encoded_input)):
   # To check if the data is empty or not if not the count will be assigned to 1       
   if (data==''):
      count = 1
   # To check if the iterated input string index character is equal to the character stored in the data or not, If its equal the count value will get increased to 1   
   elif (encoded_input[i]==data):
      count = count + 1
   # The below else part will be achieved when the abive two condition fails, will be succeed only when the previous and next character in a string are not equal, so the count will get assigned to 1 to calculate the new string.      
   else:
      encoded_output = encoded_output+str(count)+data
      count = 1
   # storing the each iterated inout string data in data variable   
   data = encoded_input[i]
  # The encoded output will store the previous concatenated output value, its count and each iterated data stored in data variable.  
  encoded_output = encoded_output+str(count)+data
  #Returning encoded output for the function encode
  return("Encoded_Output value is "+ encoded_output)

print (encode("aaaabbbbccccdddd"))
