def e(input_data):
  b = ''
  d = ''
  count = 0
  # Creating a for loop to iterate the given input string value from 0 to the length of the input string in-order to achieve all the input string data
  for i in range(1,len(input_data)-1):
   # The below condition will be pass at the first run to calculate the first string count   
   if (d==''):
    count = 1
   # The below condition will pass while comparing the input_data[0 to it's len] matches with the value stored in d, This will match only when the character repeats ; then  the count will get increamented to 1 
   elif (input_data[i]==d):
    count = count+1 
   else:
    # The below condition will pass when the above two condtions fails, or in the other words when d value is not empty and the iterated input data is not matching with the value stored in d (different character), then the count will be initialized to 1 for a new character. 
    b = b+str(count)+d
    count = 1
   # storing each iteration value in d
   d = input_data[i]
  # The b will store the final result  
  b = b+str(count)+d
  return(b)
encodedoutput = e("BBOO")
print("Encoded Output: "+ encodedoutput)
