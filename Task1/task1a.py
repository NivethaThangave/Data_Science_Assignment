def encode(input_data):
  encoded_output = ''
  data = ''
  count = 0
  # Creating a for loop to iterate the given input string value from 0 to the length of the input string in-order to achieve all the input string data
  for i in range(1,len(input_data)-1):
   # The below condition will be pass at the first run to calculate the first string count   
   if (data==''):
    count = 1
   # The below condition will pass while comparing the input_data[0 to it's len] matches with the value stored in data, This will match only when the character repeats ; then  the count will get increamented to 1 
   elif (input_data[i]==data):
    count = count+1 
   else:
    # The below condition will pass when the above two condtions fails, or in the other words when data value is not empty and the iterated input data is not matching with the value stored in data (different character), then the count will be initialized to 1 for a new character. 
    encoded_output = encoded_output+str(count)+data
    count = 1
   # storing each iteration value in data
   data = input_data[i]
  # The encoded_output will store the final result which concatenate the previous encoded_output value, its count and the each iterated data stored in data variable.
  encoded_output = encoded_output+str(count)+data
  return(encoded_output)
#calling the function encode and storing the result in output_data 
output_data = encode("BBOO")
print("Output Data: "+ output_data)
